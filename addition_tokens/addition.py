"""Smart Token Chip GUI prototype for the word-enabled addition calculator.

Features:
- Preserves three representations of each addend (ordered subcolumns, parsed mathematical structure, aggregated results).
- Independent structural precedence (visual column alignment) and mathematical precedence (evaluation order).
- Central keypad console driving all input with three navigation actions:
  Next Subcolumn (→), Next Column (⇒), and Next Addend (↓).
- Clean display cells free of permanent dropdown comboboxes.
- Adjacent label subcolumns for individual mathematical values.
- Separate Addend and Label row types.
- Bottom-anchored keypad layout preserving keypad positioning (0 button anchor).
"""

from decimal import Decimal
from pathlib import Path
import sys
import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict, List, Optional, Tuple

_PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from addition_tokens.token_model import (
    Token,
    TokenType,
    RowType,
    Subcolumn,
    SemanticTerm,
    AddendRepresentation,
    GridRow,
    ParseResult,
    TokenModelParser,
    TokenGridModel,
    is_valid_number,
)


class AdditionTokenCalculator:
    """Tkinter GUI for the Smart Token Chip Word-Enabled Addition Calculator."""

    QUICK_UNITS = ["pens", "pencils", "books", "apples", "oranges", "cars"]
    QUICK_CONTEXTS = ["in the drawer", "on the desk", "in the room", "in the basket"]

    def __init__(self, root: Optional[tk.Tk] = None) -> None:
        self._owns_root = root is None
        self.root = root if root is not None else tk.Tk()
        self.root.title("Smart Token Addition Calculator (Central Keypad & Subcolumns)")
        self.root.geometry("880x820")
        self.root.minsize(750, 650)

        # Internal Grid Model
        self.grid_model = TokenGridModel()
        self.last_parse_result: Optional[ParseResult] = None

        # Build UI layout
        self._build_ui()
        self._setup_bindings()

        # Initial render
        self.render_grid()

    # -------------------------------------------------------------------------
    # Backward Compatibility Helpers
    # -------------------------------------------------------------------------
    @property
    def rows_tokens(self) -> List[List[Token]]:
        """Adapter providing row token lists for backward compatibility with previous tests."""
        result: List[List[Token]] = []
        for r in self.grid_model.rows:
            if r.row_type == RowType.ADDEND:
                row_toks: List[Token] = []
                for addend in r.addend_columns:
                    row_toks.extend([sc.to_token() for sc in addend.ordered_subcolumns])
                result.append(row_toks)
        return result if result else [[]]

    @property
    def active_row_idx(self) -> int:
        return self.grid_model.cursor_row

    @active_row_idx.setter
    def active_row_idx(self, val: int) -> None:
        if 0 <= val < len(self.grid_model.rows):
            self.grid_model.cursor_row = val

    def add_addend_row(self) -> int:
        idx = self.grid_model.next_addend()
        self.render_grid()
        return idx

    def add_token(
        self,
        row_idx: int,
        value: str,
        token_type: Optional[TokenType] = None
    ) -> Token:
        if not (0 <= row_idx < len(self.grid_model.rows)):
            row_idx = 0
        self.grid_model.cursor_row = row_idx
        self.grid_model.cursor_area = "addend"
        self.grid_model.cursor_addend_col = 0
        row = self.grid_model.rows[row_idx]
        if not row.addend_columns:
            row.addend_columns.append(AddendRepresentation())
        addend = row.addend_columns[0]
        self.grid_model.cursor_subcol = len(addend.ordered_subcolumns)
        subcol = self.grid_model.input_value(value, token_type)
        self.render_grid()
        return subcol.to_token()

    def set_token_value(self, row_idx: int, token_idx: int, val: str) -> None:
        if 0 <= row_idx < len(self.grid_model.rows):
            row = self.grid_model.rows[row_idx]
            if row.addend_columns and 0 <= token_idx < len(row.addend_columns[0].ordered_subcolumns):
                subcol = row.addend_columns[0].ordered_subcolumns[token_idx]
                subcol.value = val
                if not subcol.explicit_type:
                    subcol.token_type = Token.auto_classify(val)
                self.render_grid()

    def set_token_type(self, row_idx: int, token_idx: int, new_type: TokenType) -> None:
        if 0 <= row_idx < len(self.grid_model.rows):
            row = self.grid_model.rows[row_idx]
            if row.addend_columns and 0 <= token_idx < len(row.addend_columns[0].ordered_subcolumns):
                subcol = row.addend_columns[0].ordered_subcolumns[token_idx]
                subcol.token_type = new_type
                subcol.explicit_type = True
                self.render_grid()

    def remove_token(self, row_idx: int, token_idx: int) -> None:
        if 0 <= row_idx < len(self.grid_model.rows):
            row = self.grid_model.rows[row_idx]
            if row.addend_columns and 0 <= token_idx < len(row.addend_columns[0].ordered_subcolumns):
                row.addend_columns[0].ordered_subcolumns.pop(token_idx)
                self.render_grid()

    def get_tokens(self, row_idx: Optional[int] = None) -> List[Token]:
        if row_idx is not None:
            if 0 <= row_idx < len(self.grid_model.rows):
                row = self.grid_model.rows[row_idx]
                if row.row_type == RowType.ADDEND and row.addend_columns:
                    return [sc.to_token() for sc in row.addend_columns[0].ordered_subcolumns if sc.value.strip()]
            return []

        # All rows
        combined: List[Token] = []
        for row in self.grid_model.rows:
            if row.row_type != RowType.ADDEND:
                continue
            row_toks: List[Token] = []
            for addend in row.addend_columns:
                addend_toks = [sc.to_token() for sc in addend.ordered_subcolumns if sc.value.strip()]
                if not addend_toks:
                    continue
                if row_toks:
                    if row_toks[-1].token_type != TokenType.OPERATOR and addend_toks[0].token_type != TokenType.OPERATOR:
                        row_toks.append(Token(value="+", token_type=TokenType.OPERATOR, explicit_type=True))
                row_toks.extend(addend_toks)

            if not row_toks:
                continue

            for desc in row.description_columns:
                if desc.strip():
                    row_toks.append(Token(value=desc.strip(), token_type=TokenType.CONTEXT))

            if combined:
                if combined[-1].token_type != TokenType.OPERATOR and row_toks[0].token_type != TokenType.OPERATOR:
                    combined.append(Token(value="+", token_type=TokenType.OPERATOR, explicit_type=True))
            combined.extend(row_toks)
        return combined

    def get_last_parse_result(self) -> Optional[ParseResult]:
        return self.last_parse_result

    # -------------------------------------------------------------------------
    # UI Layout Construction
    # -------------------------------------------------------------------------

    def _build_ui(self) -> None:
        # 1. Bottom Container anchored to bottom
        self.bottom_container = tk.Frame(self.root, bg="#f5f5f5", bd=1, relief="ridge")
        self.bottom_container.pack(side="bottom", fill="x", padx=10, pady=(4, 10))

        # Bottom Keypad Console
        self.keypad_frame = tk.Frame(self.bottom_container, bg="#f5f5f5")
        self.keypad_frame.pack(side="left", padx=8, pady=8)
        self._build_keypad()

        # Vocabulary / Central Label Console
        self.vocab_frame = tk.LabelFrame(
            self.bottom_container,
            text="Central Label Console (Inputs to Active Cell)",
            font=("Segoe UI", 9, "bold"),
            bg="#f5f5f5",
            fg="#1565c0",
        )
        self.vocab_frame.pack(side="left", fill="y", padx=6, pady=8)
        self._build_vocab_console()

        # Three Representations Inspector Frame
        self.inspector_frame = tk.LabelFrame(
            self.bottom_container,
            text="Addend Representations Inspector (1: Subcols | 2: Parsed | 3: Aggregated)",
            font=("Segoe UI", 9, "bold"),
            bg="#f5f5f5",
            fg="#2e7d32",
        )
        self.inspector_frame.pack(side="left", fill="both", expand=True, padx=8, pady=8)

        self.inspector_text = tk.Text(
            self.inspector_frame,
            height=8,
            font=("Consolas", 9),
            bg="#ffffff",
            fg="#333333",
            relief="sunken",
            bd=1,
            wrap="word",
        )
        self.inspector_text.pack(fill="both", expand=True, padx=4, pady=4)
        self.inspector_text.insert("1.0", "Use central keypad to enter subcolumns. Press '=' to evaluate representations.")
        self.inspector_text.configure(state="disabled")

        # 2. Result Summary Frame (just above bottom controls)
        self.result_frame = tk.Frame(self.root, bg="#ffffff", bd=2, relief="groove")
        self.result_frame.pack(side="bottom", fill="x", padx=10, pady=4)

        res_lbl = tk.Label(
            self.result_frame,
            text="Result Summary:",
            font=("Segoe UI", 9, "bold"),
            bg="#ffffff",
            fg="#1b5e20",
            anchor="w",
        )
        res_lbl.pack(fill="x", padx=8, pady=(4, 2))

        result_row = tk.Frame(self.result_frame, bg="#ffffff")
        result_row.pack(fill="x", expand=True, padx=8, pady=(0, 6))

        self.result_var = tk.StringVar(value="")
        self.result_entry = tk.Entry(
            result_row,
            textvariable=self.result_var,
            font=("Consolas", 14, "bold"),
            justify="right",
            state="readonly",
            readonlybackground="#f4f9f4",
            fg="#1b5e20",
            bd=2,
            relief="sunken",
            width=12,
        )
        self.result_entry.pack(side="left")

        self.result_word_var = tk.StringVar(value="")
        self.result_word_entry = tk.Entry(
            result_row,
            textvariable=self.result_word_var,
            font=("Segoe UI", 12, "bold"),
            justify="left",
            state="readonly",
            readonlybackground="#f4f9f4",
            fg="#1b5e20",
            bd=2,
            relief="sunken",
        )
        self.result_word_entry.pack(side="left", fill="x", expand=True, padx=(8, 0))

        # 3. Top Action / Status Bar
        self.top_bar = tk.Frame(self.root, bg="#e8f5e9", bd=1, relief="ridge")
        self.top_bar.pack(side="top", fill="x", padx=10, pady=(10, 4))

        title_lbl = tk.Label(
            self.top_bar,
            text="Smart Token Expression Builder (Central Keypad Console)",
            font=("Segoe UI", 11, "bold"),
            bg="#e8f5e9",
            fg="#1b5e20",
        )
        title_lbl.pack(side="left", padx=10, pady=6)

        btn_style = {"font": ("Segoe UI", 9, "bold"), "relief": "raised", "bd": 2, "padx": 6}

        self.calc_btn = tk.Button(
            self.top_bar,
            text="Calculate (=)",
            bg="#1976d2",
            fg="#ffffff",
            command=self.calculate,
            **btn_style,
        )
        self.calc_btn.pack(side="left", padx=4, pady=6)

        self.clear_btn = tk.Button(
            self.top_bar,
            text="Clear (C)",
            bg="#d32f2f",
            fg="#ffffff",
            command=self.clear,
            **btn_style,
        )
        self.clear_btn.pack(side="left", padx=4, pady=6)

        self.add_label_btn = tk.Button(
            self.top_bar,
            text="+ Label Row",
            bg="#7b1fa2",
            fg="#ffffff",
            command=lambda: self.add_label_row("Descriptive Note"),
            **btn_style,
        )
        self.add_label_btn.pack(side="left", padx=4, pady=6)

        # 4. Center Scrollable Container for Clean Display Grid
        self.scroll_container = tk.Frame(self.root, bg="#ffffff", bd=1, relief="sunken")
        self.scroll_container.pack(side="top", fill="both", expand=True, padx=10, pady=4)

        self.canvas = tk.Canvas(self.scroll_container, bg="#ffffff", highlightthickness=0, bd=0)
        self.scrollbar = tk.Scrollbar(self.scroll_container, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.grid_frame = tk.Frame(self.canvas, bg="#ffffff")
        self.canvas_window_id = self.canvas.create_window((0, 0), window=self.grid_frame, anchor="nw")

        self.grid_frame.bind("<Configure>", lambda _e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self.canvas_window_id, width=e.width))

    def _build_keypad(self) -> None:
        """Constructs bottom-anchored keypad with the 3 explicit navigation actions."""
        buttons = [
            ("(", 0, 0), (")", 0, 1), ("C", 0, 2), ("+", 0, 3),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("Next Subcol (→)", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("Next Col (⇒)", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("Next Addend (↓)", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("Backspace", 4, 2), ("=", 4, 3),
        ]

        self.keypad_buttons: Dict[str, tk.Button] = {}

        for text, r, c in buttons:
            cmd = lambda val=text: self._on_keypad_press(val)
            bg = "#e0e0e0"
            fg = "#000000"
            if text in ("=", "Next Addend (↓)"):
                bg = "#4caf50"
                fg = "#ffffff"
            elif text == "C":
                bg = "#f44336"
                fg = "#ffffff"
            elif text in ("(", ")", "+"):
                bg = "#bbdefb"
                fg = "#0d47a1"
            elif "Next" in text:
                bg = "#fff9c4"
                fg = "#f57f17"

            btn = tk.Button(
                self.keypad_frame,
                text=text,
                font=("Segoe UI", 9, "bold"),
                width=12 if "Next" in text or text == "Backspace" else 6,
                height=1,
                bg=bg,
                fg=fg,
                relief="raised",
                bd=2,
                command=cmd,
            )
            btn.grid(row=r, column=c, padx=2, pady=2, sticky="nsew")
            self.keypad_buttons[text] = btn

    def _build_vocab_console(self) -> None:
        """Builds central vocabulary controls to feed labels directly to the active cell."""
        u_frame = tk.Frame(self.vocab_frame, bg="#f5f5f5")
        u_frame.pack(fill="x", padx=4, pady=2)
        tk.Label(u_frame, text="Units:", font=("Segoe UI", 8, "bold"), bg="#f5f5f5").pack(side="left")
        for u in self.QUICK_UNITS:
            btn = tk.Button(
                u_frame,
                text=u,
                font=("Segoe UI", 8),
                bg="#e1f5fe",
                command=lambda val=u: self._on_vocab_click(val, TokenType.ITEM),
            )
            btn.pack(side="left", padx=2)

        c_frame = tk.Frame(self.vocab_frame, bg="#f5f5f5")
        c_frame.pack(fill="x", padx=4, pady=2)
        tk.Label(c_frame, text="Context:", font=("Segoe UI", 8, "bold"), bg="#f5f5f5").pack(side="left")
        for c in self.QUICK_CONTEXTS:
            btn = tk.Button(
                c_frame,
                text=c,
                font=("Segoe UI", 8),
                bg="#fce4ec",
                command=lambda val=c: self._on_vocab_click(val, TokenType.CONTEXT),
            )
            btn.pack(side="left", padx=2)

        entry_frame = tk.Frame(self.vocab_frame, bg="#f5f5f5")
        entry_frame.pack(fill="x", padx=4, pady=4)
        self.custom_label_var = tk.StringVar(value="")
        self.custom_label_entry = tk.Entry(entry_frame, textvariable=self.custom_label_var, font=("Segoe UI", 9), width=14)
        self.custom_label_entry.pack(side="left", padx=2)
        apply_btn = tk.Button(
            entry_frame,
            text="Apply Label",
            font=("Segoe UI", 8, "bold"),
            bg="#e8f5e9",
            fg="#2e7d32",
            command=self._on_apply_custom_label,
        )
        apply_btn.pack(side="left", padx=2)

    def _setup_bindings(self) -> None:
        self.root.bind("<Return>", lambda _e: self.calculate())
        self.root.bind("<KP_Enter>", lambda _e: self.calculate())
        self.root.bind("<Escape>", lambda _e: self.clear())

    # -------------------------------------------------------------------------
    # Keypad & Input Handling
    # -------------------------------------------------------------------------

    def _on_keypad_press(self, val: str) -> None:
        if val == "=":
            self.calculate()
        elif val == "C":
            self.clear()
        elif val == "Backspace":
            self.grid_model.backspace()
            self.render_grid()
        elif val == "Next Subcol (→)":
            self.grid_model.next_subcolumn()
            self.render_grid()
        elif val == "Next Col (⇒)":
            self.grid_model.next_column()
            self.render_grid()
        elif val == "Next Addend (↓)":
            self.grid_model.next_addend()
            self.render_grid()
        else:
            # Feeds value (0-9, ., +, (, )) to active subcolumn
            self.grid_model.input_value(val)
            self.render_grid()

    def _on_vocab_click(self, val: str, t_type: TokenType) -> None:
        self.grid_model.input_value(val, t_type)
        self.render_grid()

    def _on_apply_custom_label(self) -> None:
        lbl = self.custom_label_var.get().strip()
        if lbl:
            self.grid_model.input_value(lbl, TokenType.ITEM)
            self.custom_label_var.set("")
            self.render_grid()

    def add_label_row(self, text: str = "Descriptive Annotation") -> int:
        idx = self.grid_model.add_label_row(text)
        self.render_grid()
        return idx

    # -------------------------------------------------------------------------
    # Clean Display Grid Rendering (NO PERMANENT DROPDOWNS)
    # -------------------------------------------------------------------------

    def render_grid(self) -> None:
        """
        Renders clean display cells with independent structural precedence:
        Addend columns appear before descriptive columns, and adding more
        addend columns shifts descriptive columns to the right across all rows.
        """
        for child in self.grid_frame.winfo_children():
            child.destroy()

        max_addend_cols = self.grid_model.get_max_addend_columns()

        # Grid Header
        header_bar = tk.Frame(self.grid_frame, bg="#e0e0e0", bd=1, relief="ridge")
        header_bar.pack(fill="x", padx=4, pady=2)
        tk.Label(header_bar, text="Row", font=("Segoe UI", 9, "bold"), width=10, bg="#e0e0e0").pack(side="left")
        for i in range(max_addend_cols):
            tk.Label(
                header_bar,
                text=f"Addend Column {i + 1} (Subcolumns)",
                font=("Segoe UI", 9, "bold"),
                fg="#1b5e20",
                bg="#e0e0e0",
                padx=8,
            ).pack(side="left", padx=4)
        tk.Label(
            header_bar,
            text="Descriptive Columns (Pushed to Right)",
            font=("Segoe UI", 9, "bold"),
            fg="#6a1b9a",
            bg="#e0e0e0",
            padx=8,
        ).pack(side="left", padx=4)

        # Render Each Row
        for r_idx, row in enumerate(self.grid_model.rows):
            is_active_row = (r_idx == self.grid_model.cursor_row)
            row_bg = "#ffffff" if not is_active_row else "#fffde7"

            row_card = tk.Frame(self.grid_frame, bg=row_bg, bd=1, relief="solid")
            row_card.pack(fill="x", expand=True, padx=4, pady=3)

            # Row Header Tag
            if row.row_type == RowType.LABEL:
                tag_lbl = tk.Label(
                    row_card,
                    text=f"[Label Row {r_idx + 1}]",
                    font=("Segoe UI", 9, "bold"),
                    bg="#ede7f6",
                    fg="#4a148c",
                    width=12,
                )
                tag_lbl.pack(side="left", padx=4, pady=4)

                lbl_val = tk.Label(
                    row_card,
                    text=row.label_text or "(Empty descriptive label)",
                    font=("Segoe UI", 10, "italic"),
                    bg=row_bg,
                    fg="#333333",
                )
                lbl_val.pack(side="left", padx=8, pady=4)
                continue

            # Addend Row
            tag_text = f"Addend {r_idx + 1}" if r_idx == 0 else f"Addend {r_idx + 1} (+)"
            tag_lbl = tk.Label(
                row_card,
                text=tag_text,
                font=("Segoe UI", 9, "bold"),
                bg="#e8f5e9",
                fg="#1b5e20",
                width=12,
            )
            tag_lbl.pack(side="left", padx=4, pady=4)

            # Addend Columns (containing subcolumns)
            for c_idx in range(max_addend_cols):
                col_frame = tk.Frame(row_card, bg="#fafafa", bd=1, relief="groove")
                col_frame.pack(side="left", padx=4, pady=4)

                if c_idx < len(row.addend_columns):
                    addend = row.addend_columns[c_idx]
                    if not addend.ordered_subcolumns:
                        # Empty placeholder cell
                        is_active_cell = (
                            is_active_row and
                            self.grid_model.cursor_area == "addend" and
                            self.grid_model.cursor_addend_col == c_idx and
                            self.grid_model.cursor_subcol == 0
                        )
                        bd_col = "#2e7d32" if is_active_cell else "#cccccc"
                        cell = tk.Label(
                            col_frame,
                            text="[ empty ]",
                            font=("Segoe UI", 9),
                            fg="#999999",
                            bg="#ffffff",
                            bd=2 if is_active_cell else 1,
                            relief="solid",
                            padx=6,
                            pady=2,
                        )
                        cell.pack(side="left", padx=2, pady=2)
                    else:
                        for s_idx, sc in enumerate(addend.ordered_subcolumns):
                            is_active_cell = (
                                is_active_row and
                                self.grid_model.cursor_area == "addend" and
                                self.grid_model.cursor_addend_col == c_idx and
                                self.grid_model.cursor_subcol == s_idx
                            )
                            self._render_clean_subcol_cell(col_frame, sc, is_active_cell)
                else:
                    # Row has fewer addend columns than the maximum: display empty spacer
                    spacer = tk.Label(col_frame, text="—", font=("Segoe UI", 9), fg="#cccccc", bg="#fafafa", width=6)
                    spacer.pack(side="left", padx=4, pady=2)

            # Descriptive Columns (Pushed to the right of all addend columns)
            desc_frame = tk.Frame(row_card, bg="#f3e5f5", bd=1, relief="groove")
            desc_frame.pack(side="left", padx=6, pady=4)

            if not row.description_columns:
                tk.Label(desc_frame, text="(No descriptive tags)", font=("Segoe UI", 8, "italic"), fg="#777777", bg="#f3e5f5").pack(side="left", padx=4)
            else:
                for d_idx, desc in enumerate(row.description_columns):
                    is_active_desc = (
                        is_active_row and
                        self.grid_model.cursor_area == "description" and
                        self.grid_model.cursor_desc_col == d_idx
                    )
                    d_cell = tk.Label(
                        desc_frame,
                        text=desc or "[empty]",
                        font=("Segoe UI", 9, "bold"),
                        fg="#4a148c",
                        bg="#ffffff",
                        bd=2 if is_active_desc else 1,
                        relief="solid",
                        padx=6,
                        pady=2,
                    )
                    d_cell.pack(side="left", padx=2, pady=2)

    def _render_clean_subcol_cell(self, parent: tk.Widget, sc: Subcolumn, is_active: bool) -> tk.Widget:
        """Renders a clean subcolumn pill/box with NO permanent dropdowns."""
        type_colors = {
            TokenType.GROUP_OPEN: ("#e3f2fd", "#0d47a1"),
            TokenType.GROUP_CLOSE: ("#e3f2fd", "#0d47a1"),
            TokenType.OPERATOR: ("#fff3e0", "#e65100"),
            TokenType.NUMBER: ("#e8f5e9", "#1b5e20"),
            TokenType.ITEM: ("#f3e5f5", "#6a1b9a"),
            TokenType.CONTEXT: ("#fce4ec", "#880e4f"),
        }
        bg_col, fg_col = type_colors.get(sc.token_type, ("#ffffff", "#333333"))

        bd_width = 2 if is_active else 1
        relief = "solid" if is_active else "ridge"
        highlight_bg = "#ffeb3b" if is_active else bg_col

        cell = tk.Label(
            parent,
            text=sc.value,
            font=("Segoe UI", 9, "bold" if sc.token_type in (TokenType.NUMBER, TokenType.OPERATOR) else "normal"),
            bg=highlight_bg,
            fg=fg_col,
            bd=bd_width,
            relief=relief,
            padx=6,
            pady=2,
        )
        cell.pack(side="left", padx=2, pady=2)
        return cell

    # -------------------------------------------------------------------------
    # Calculation & Three Representations Inspector
    # -------------------------------------------------------------------------

    def calculate(self) -> Optional[ParseResult]:
        """Calculates global result and updates the three representations inspector."""
        parse_res = self.grid_model.calculate()
        self.last_parse_result = parse_res

        if not parse_res:
            self.result_var.set("")
            self.result_word_var.set("Expression is empty")
            return None

        self.result_var.set(parse_res.total_number)
        self.result_word_var.set(parse_res.word_result)

        # Update Inspector Text with the Three Representations (Refinement 1)
        self.inspector_text.configure(state="normal")
        self.inspector_text.delete("1.0", "end")

        output_lines = [
            f"=== TOTAL SUMMARY ===",
            f"Math Total: {parse_res.total_number}",
            f"Sentence Result: {parse_res.word_result}",
            f"\n=== ADDEND REPRESENTATIONS (Refinement 1) ===",
        ]

        addend_count = 0
        for r_idx, row in enumerate(self.grid_model.rows):
            if row.row_type != RowType.ADDEND:
                output_lines.append(f"\n[Row {r_idx + 1}: Label Row] — '{row.label_text}'")
                continue

            for c_idx, addend in enumerate(row.addend_columns):
                addend_count += 1
                output_lines.append(f"\n--- Addend {addend_count} (Row {r_idx + 1}, Col {c_idx + 1}) ---")

                # Rep 1: Ordered Subcolumns
                subcol_str = " | ".join(f"'{sc.value}'" for sc in addend.ordered_subcolumns)
                output_lines.append(f"  Rep 1 (Ordered Subcolumns): [{subcol_str}]")

                # Rep 2: Parsed Mathematical Structure (Unaggregated)
                output_lines.append(f"  Rep 2 (Parsed Structure - Unaggregated):")
                if not addend.parsed_terms:
                    output_lines.append("    (No parsed terms)")
                for t in addend.parsed_terms:
                    ctx = f", context='{t.context}'" if t.context else ""
                    output_lines.append(f"    Quantity: {t.quantity}, Unit: '{t.item}'{ctx}")

                # Rep 3: Aggregated Results by Compatible Units
                output_lines.append(f"  Rep 3 (Aggregated Results by Units):")
                if not addend.aggregated_results:
                    output_lines.append("    (No aggregated terms)")
                for t in addend.aggregated_results:
                    ctx = f" {t.context}" if t.context else ""
                    output_lines.append(f"    Subtotal: {t.quantity} {t.item}{ctx}")

        self.inspector_text.insert("1.0", "\n".join(output_lines))
        self.inspector_text.configure(state="disabled")

        self.render_grid()
        return parse_res

    def clear(self) -> None:
        """Resets the model, outputs, and grid."""
        self.grid_model.clear()
        self.last_parse_result = None
        self.result_var.set("")
        self.result_word_var.set("")

        self.inspector_text.configure(state="normal")
        self.inspector_text.delete("1.0", "end")
        self.inspector_text.insert("1.0", "Cleared.")
        self.inspector_text.configure(state="disabled")

        self.render_grid()

    def run(self) -> None:
        if self._owns_root:
            self.root.mainloop()


def main() -> None:
    app = AdditionTokenCalculator()
    app.run()


if __name__ == "__main__":
    main()
