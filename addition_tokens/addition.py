"""Smart Token Chip GUI prototype for the word-enabled addition calculator.

Features:
- Mathematical templates in Column 1 with named, typed editable value slots (□).
- Central keypad console driving input into selected slots.
- Template preview from pasted addition expressions (e.g. '(15.5 + 4.25) + 8.0' or '(□ + □) + □').
- Optional template saving: templates can be previewed, reviewed, and optionally saved to custom_templates.json.
- Columns 2 and beyond are reserved for descriptive labels (Item, Context, etc.).
- Explicit 'Next Row' control asking user for row type (Addend Row, Label Row, or future Algebra Step).
- Clean display cells free of permanent dropdown menus.
- Safe GUI error handling: catches parser validation errors without uncaught exceptions.
- Bottom-anchored keypad layout preserving keypad positioning (0 button anchor).
- Synchronized column width calculation and horizontal scrolling preventing expression displacement.
- Dedicated, resizable, scrollable Results Window (ttk.PanedWindow) with text size controls, wrapping toggle, and clipboard copy.
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
    SlotMetadata,
    TemplateSlot,
    MathTemplate,
    TemplateValidator,
    ExpressionTemplateParser,
    MathTemplateManager,
    TemplateInstance,
    TemplateRow,
    TemplateGridModel,
    is_valid_number,
)


class AdditionTokenCalculator:
    """Tkinter GUI for the Template-Driven Smart Token Addition Calculator."""

    QUICK_UNITS = ["pens", "pencils", "books", "apples", "oranges", "cars"]
    QUICK_CONTEXTS = ["in the drawer", "on the desk", "in the room", "in the basket"]

    def __init__(self, root: Optional[tk.Tk] = None) -> None:
        self._owns_root = root is None
        self.root = root if root is not None else tk.Tk()
        self.root.title("Smart Token Addition Calculator (Math Templates & Central Input)")
        self.root.geometry("960x900")
        self.root.minsize(800, 700)

        # Template and Grid Models
        self.template_manager = MathTemplateManager()
        self.template_grid_model = TemplateGridModel(self.template_manager)
        self.grid_model = TokenGridModel()  # Kept for backward compatibility
        self.last_parse_result: Optional[ParseResult] = None
        self.current_preview_template: Optional[MathTemplate] = None

        # Build UI layout
        self._build_ui()
        self._setup_bindings()

        # Initial render
        self.render_grid()

    # -------------------------------------------------------------------------
    # Backward Compatibility Adapter Properties
    # -------------------------------------------------------------------------
    @property
    def rows_tokens(self) -> List[List[Token]]:
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
        self.template_grid_model.add_row(RowType.ADDEND)
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
        self.grid_model.select_cell(row_idx, "addend", 0, 0)
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
        # 1. Bottom Container anchored firmly to the bottom of the window
        # Contains: Central Keypad, Center Vocab/Templates Console, Inspector
        self.bottom_container = tk.Frame(self.root, bg="#f5f5f5", bd=1, relief="ridge")
        self.bottom_container.pack(side="bottom", fill="x", padx=10, pady=(4, 10))

        # Bottom Keypad Console
        self.keypad_frame = tk.Frame(self.bottom_container, bg="#f5f5f5")
        self.keypad_frame.pack(side="left", padx=8, pady=8)
        self._build_keypad()

        # Center Template & Vocabulary Console
        self.center_console = tk.Frame(self.bottom_container, bg="#f5f5f5")
        self.center_console.pack(side="left", fill="y", padx=6, pady=8)
        self._build_template_console()
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

        self.inspector_scroll_y = tk.Scrollbar(self.inspector_frame, orient="vertical")
        self.inspector_scroll_y.pack(side="right", fill="y")

        self.inspector_text = tk.Text(
            self.inspector_frame,
            height=8,
            font=("Consolas", 9),
            bg="#ffffff",
            fg="#333333",
            relief="sunken",
            bd=1,
            wrap="word",
            yscrollcommand=self.inspector_scroll_y.set,
        )
        self.inspector_scroll_y.config(command=self.inspector_text.yview)
        self.inspector_text.pack(fill="both", expand=True, padx=4, pady=4)
        self.inspector_text.insert("1.0", "Select a template for Column 1, click editable slots (□), and enter values via keypad.")
        self.inspector_text.configure(state="disabled")

        # 2. Top Action / Selection Status Bar
        self.top_bar = tk.Frame(self.root, bg="#e8f5e9", bd=1, relief="ridge")
        self.top_bar.pack(side="top", fill="x", padx=10, pady=(10, 4))

        title_lbl = tk.Label(
            self.top_bar,
            text="Smart Token Expression Builder (Math Templates)",
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

        self.next_row_btn = tk.Button(
            self.top_bar,
            text="Next Row (↓)",
            bg="#388e3c",
            fg="#ffffff",
            command=self._prompt_next_row_type,
            **btn_style,
        )
        self.next_row_btn.pack(side="left", padx=4, pady=6)

        self.add_desc_col_btn = tk.Button(
            self.top_bar,
            text="+ Add Description Col",
            bg="#8e24aa",
            fg="#ffffff",
            command=self.add_description_column,
            **btn_style,
        )
        self.add_desc_col_btn.pack(side="left", padx=4, pady=6)

        self.del_col_btn = tk.Button(
            self.top_bar,
            text="Delete Selected Col",
            bg="#ff7043",
            fg="#ffffff",
            command=self.delete_selected_column,
            **btn_style,
        )
        self.del_col_btn.pack(side="left", padx=4, pady=6)

        # Selection Status Indicator Banner
        self.status_bar = tk.Frame(self.root, bg="#fffde7", bd=1, relief="solid")
        self.status_bar.pack(side="top", fill="x", padx=10, pady=(2, 4))

        self.selection_status_var = tk.StringVar(value="Selected Target: Row 1 | Column 1 (Math Template)")
        self.selection_status_lbl = tk.Label(
            self.status_bar,
            textvariable=self.selection_status_var,
            font=("Segoe UI", 10, "bold"),
            bg="#fffde7",
            fg="#e65100",
            anchor="w",
            padx=8,
            pady=3,
        )
        self.selection_status_lbl.pack(fill="x")

        # 3. Vertical PanedWindow: Divides Mathematical Grid (Top Pane) and Results Window (Bottom Pane)
        # Positioned right between Status Bar and Bottom Keypad Console
        self.main_paned = ttk.PanedWindow(self.root, orient="vertical")
        self.main_paned.pack(side="top", fill="both", expand=True, padx=10, pady=4)

        # Upper Pane: Mathematical Grid Scrollable Container (Canvas + Scrollbars)
        self.scroll_container = tk.Frame(self.main_paned, bg="#ffffff", bd=1, relief="sunken")
        self.main_paned.add(self.scroll_container, weight=3)

        self.canvas = tk.Canvas(self.scroll_container, bg="#ffffff", highlightthickness=0, bd=0)
        self.scrollbar = tk.Scrollbar(self.scroll_container, orient="vertical", command=self.canvas.yview)
        self.scrollbar_y = self.scrollbar  # Backward compatibility alias
        self.scrollbar_x = tk.Scrollbar(self.scroll_container, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set, xscrollcommand=self.scrollbar_x.set)

        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar_x.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.total_grid_content_width = 800

        self.grid_frame = tk.Frame(self.canvas, bg="#ffffff")
        self.canvas_window_id = self.canvas.create_window((0, 0), window=self.grid_frame, anchor="nw")

        self.grid_frame.bind("<Configure>", self._on_grid_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)

        # Lower Pane: Dedicated, Resizable, Scrollable Results Window
        self._build_results_panel()

    def _build_results_panel(self) -> None:
        """Constructs dedicated multiline, resizable, scrollable Results Window with toolbar controls."""
        self.result_frame = tk.Frame(self.main_paned, bg="#ffffff", bd=2, relief="groove")
        self.main_paned.add(self.result_frame, weight=2)

        self.results_font_size = 10
        self.results_wrap_mode = True
        self.results_expanded = False

        # Results Toolbar
        res_header = tk.Frame(self.result_frame, bg="#f1f8e9", bd=1, relief="ridge")
        res_header.pack(side="top", fill="x", padx=2, pady=2)

        res_lbl = tk.Label(
            res_header,
            text="Detailed Results & Mathematical Analysis:",
            font=("Segoe UI", 9, "bold"),
            bg="#f1f8e9",
            fg="#1b5e20",
            anchor="w",
        )
        res_lbl.pack(side="left", padx=6, pady=3)

        # Numerical and word summary entries (Preserved for backward-compatibility)
        self.result_var = tk.StringVar(value="")
        self.result_entry = tk.Entry(
            res_header,
            textvariable=self.result_var,
            font=("Consolas", 11, "bold"),
            justify="right",
            state="readonly",
            readonlybackground="#e8f5e9",
            fg="#1b5e20",
            bd=1,
            relief="sunken",
            width=12,
        )
        self.result_entry.pack(side="left", padx=4, pady=2)

        self.result_word_var = tk.StringVar(value="")
        self.result_word_entry = tk.Entry(
            res_header,
            textvariable=self.result_word_var,
            font=("Segoe UI", 9),
            justify="left",
            state="readonly",
            readonlybackground="#ffffff",
            fg="#333333",
            bd=1,
            relief="sunken",
            width=24,
        )
        self.result_word_entry.pack(side="left", padx=2, pady=2)

        btn_kw = {"font": ("Segoe UI", 8, "bold"), "relief": "raised", "bd": 1, "padx": 4, "pady": 1}

        # Toolbar controls aligned right
        self.font_down_btn = tk.Button(
            res_header,
            text="A-",
            command=self.decrease_results_font,
            bg="#f5f5f5",
            **btn_kw,
        )
        self.font_down_btn.pack(side="right", padx=1)

        self.font_reset_btn = tk.Button(
            res_header,
            text="100%",
            command=self.reset_results_font,
            bg="#f5f5f5",
            **btn_kw,
        )
        self.font_reset_btn.pack(side="right", padx=1)

        self.font_up_btn = tk.Button(
            res_header,
            text="A+",
            command=self.increase_results_font,
            bg="#f5f5f5",
            **btn_kw,
        )
        self.font_up_btn.pack(side="right", padx=1)

        self.wrap_btn = tk.Button(
            res_header,
            text="Wrap: ON",
            command=self.toggle_results_wrap,
            bg="#e3f2fd",
            fg="#0d47a1",
            **btn_kw,
        )
        self.wrap_btn.pack(side="right", padx=3)

        self.copy_btn = tk.Button(
            res_header,
            text="Copy Results",
            command=self.copy_results_to_clipboard,
            bg="#ede7f6",
            fg="#4a148c",
            **btn_kw,
        )
        self.copy_btn.pack(side="right", padx=3)

        self.expand_btn = tk.Button(
            res_header,
            text="Expand ⇕",
            command=self.toggle_expand_results,
            bg="#fff3e0",
            fg="#e65100",
            **btn_kw,
        )
        self.expand_btn.pack(side="right", padx=3)

        # Multiline text container with vertical AND horizontal scrollbars
        self.results_text_container = tk.Frame(self.result_frame, bg="#ffffff")
        self.results_text_container.pack(fill="both", expand=True, padx=4, pady=2)

        self.results_scroll_y = tk.Scrollbar(self.results_text_container, orient="vertical")
        self.results_scroll_x = tk.Scrollbar(self.results_text_container, orient="horizontal")

        self.results_text = tk.Text(
            self.results_text_container,
            font=("Consolas", self.results_font_size),
            wrap="word",
            bg="#ffffff",
            fg="#1b5e20",
            bd=1,
            relief="sunken",
            yscrollcommand=self.results_scroll_y.set,
            xscrollcommand=self.results_scroll_x.set,
        )
        self.results_scroll_y.config(command=self.results_text.yview)
        self.results_scroll_x.config(command=self.results_text.xview)

        self.results_scroll_y.pack(side="right", fill="y")
        self.results_scroll_x.pack(side="bottom", fill="x")
        self.results_text.pack(side="left", fill="both", expand=True)

        self.results_text.insert("1.0", "Mathematical and descriptive calculation results will appear here.")
        self.results_text.configure(state="disabled")

    def increase_results_font(self) -> None:
        """Increases results font size without altering mathematical values."""
        if self.results_font_size < 28:
            self.results_font_size += 1
            self.results_text.configure(font=("Consolas", self.results_font_size))

    def decrease_results_font(self) -> None:
        """Decreases results font size without altering mathematical values."""
        if self.results_font_size > 7:
            self.results_font_size -= 1
            self.results_text.configure(font=("Consolas", self.results_font_size))

    def reset_results_font(self) -> None:
        """Resets results font size to standard 10pt without altering mathematical values."""
        self.results_font_size = 10
        self.results_text.configure(font=("Consolas", self.results_font_size))

    def toggle_results_wrap(self) -> None:
        """Toggles results text wrapping between word-wrap and horizontal scrolling."""
        self.results_wrap_mode = not self.results_wrap_mode
        if self.results_wrap_mode:
            self.results_text.configure(wrap="word")
            self.wrap_btn.configure(text="Wrap: ON", bg="#e3f2fd", fg="#0d47a1")
        else:
            self.results_text.configure(wrap="none")
            self.wrap_btn.configure(text="Wrap: OFF", bg="#fffde7", fg="#e65100")

    def copy_results_to_clipboard(self) -> str:
        """Copies full results text to clipboard and returns content."""
        content = self.results_text.get("1.0", "end-1c")
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(content)
        except Exception:
            pass
        return content

    def toggle_expand_results(self) -> None:
        """Toggles results panel between standard split and expanded view."""
        self.results_expanded = not self.results_expanded
        if hasattr(self, "main_paned"):
            try:
                if self.results_expanded:
                    self.main_paned.pane(self.scroll_container, weight=1)
                    self.main_paned.pane(self.result_frame, weight=4)
                    self.expand_btn.configure(text="Collapse ⇕", bg="#ffebee", fg="#c62828")
                else:
                    self.main_paned.pane(self.scroll_container, weight=3)
                    self.main_paned.pane(self.result_frame, weight=2)
                    self.expand_btn.configure(text="Expand ⇕", bg="#fff3e0", fg="#e65100")
            except Exception:
                if self.results_expanded:
                    self.expand_btn.configure(text="Collapse ⇕", bg="#ffebee", fg="#c62828")
                else:
                    self.expand_btn.configure(text="Expand ⇕", bg="#fff3e0", fg="#e65100")

    def _on_grid_frame_configure(self, _event: Optional[tk.Event] = None) -> None:
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_canvas_configure(self, event: tk.Event) -> None:
        target_w = max(event.width, getattr(self, "total_grid_content_width", 800))
        self.canvas.itemconfig(self.canvas_window_id, width=target_w)

    def _build_keypad(self) -> None:
        """Constructs bottom-anchored keypad preserving the 0 button coordinate anchor."""
        buttons = [
            ("(", 0, 0), (")", 0, 1), ("C", 0, 2), ("+", 0, 3),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("Next Slot (→)", 1, 3),
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

        # Backward compatibility alias for tests or callers referencing 'Next Subcol (→)'
        if "Next Slot (→)" in self.keypad_buttons:
            self.keypad_buttons["Next Subcol (→)"] = self.keypad_buttons["Next Slot (→)"]

    def _build_template_console(self) -> None:
        """Builds controls for selecting, previewing, and optionally saving templates."""
        self.tpl_box = tk.LabelFrame(
            self.center_console,
            text="Mathematical Templates (Column 1)",
            font=("Segoe UI", 8, "bold"),
            bg="#f5f5f5",
            fg="#1565c0",
        )
        self.tpl_box.pack(fill="x", padx=4, pady=2)

        # Dropdown of templates
        row1 = tk.Frame(self.tpl_box, bg="#f5f5f5")
        row1.pack(fill="x", padx=4, pady=2)

        self.template_patterns = [t.pattern for t in self.template_manager.templates]
        self.selected_template_var = tk.StringVar(value=self.template_patterns[0])
        self.template_combo = ttk.Combobox(
            row1,
            textvariable=self.selected_template_var,
            values=self.template_patterns,
            state="readonly",
            width=16,
            font=("Segoe UI", 9),
        )
        self.template_combo.pack(side="left", padx=2)
        self.template_combo.bind("<<ComboboxSelected>>", lambda _e: self._on_apply_selected_template())

        apply_btn = tk.Button(
            row1,
            text="Apply Template",
            font=("Segoe UI", 8, "bold"),
            bg="#e3f2fd",
            fg="#0d47a1",
            command=self._on_apply_selected_template,
        )
        apply_btn.pack(side="left", padx=2)

        # Pasted expression input & preview
        row2 = tk.Frame(self.tpl_box, bg="#f5f5f5")
        row2.pack(fill="x", padx=4, pady=2)

        self.pasted_expr_var = tk.StringVar(value="")
        self.pasted_entry = tk.Entry(
            row2,
            textvariable=self.pasted_expr_var,
            font=("Segoe UI", 9),
            width=16,
        )
        self.pasted_entry.pack(side="left", padx=2)

        preview_btn = tk.Button(
            row2,
            text="Preview Pasted",
            font=("Segoe UI", 8),
            bg="#fff3e0",
            fg="#e65100",
            command=self._on_preview_pasted_expression,
        )
        preview_btn.pack(side="left", padx=2)

        self.save_tpl_btn = tk.Button(
            row2,
            text="Save Template",
            font=("Segoe UI", 8, "bold"),
            bg="#e8f5e9",
            fg="#2e7d32",
            state="disabled",
            command=self._on_save_custom_template,
        )
        self.save_tpl_btn.pack(side="left", padx=2)

    def _build_vocab_console(self) -> None:
        """Builds central vocabulary controls to feed labels directly to the active selected cell."""
        self.vocab_frame = tk.LabelFrame(
            self.center_console,
            text="Descriptive Columns Console (Col 2 & 3)",
            font=("Segoe UI", 8, "bold"),
            bg="#f5f5f5",
            fg="#6a1b9a",
        )
        self.vocab_frame.pack(fill="x", padx=4, pady=2)

        u_frame = tk.Frame(self.vocab_frame, bg="#f5f5f5")
        u_frame.pack(fill="x", padx=4, pady=1)
        tk.Label(u_frame, text="Unit:", font=("Segoe UI", 8, "bold"), bg="#f5f5f5").pack(side="left")
        for u in self.QUICK_UNITS:
            btn = tk.Button(
                u_frame,
                text=u,
                font=("Segoe UI", 8),
                bg="#e1f5fe",
                command=lambda val=u: self._set_active_word(val),
            )
            btn.pack(side="left", padx=1)

        c_frame = tk.Frame(self.vocab_frame, bg="#f5f5f5")
        c_frame.pack(fill="x", padx=4, pady=1)
        tk.Label(c_frame, text="Context:", font=("Segoe UI", 8, "bold"), bg="#f5f5f5").pack(side="left")
        for c in self.QUICK_CONTEXTS:
            btn = tk.Button(
                c_frame,
                text=c,
                font=("Segoe UI", 8),
                bg="#fce4ec",
                command=lambda val=c: self._set_active_word(val),
            )
            btn.pack(side="left", padx=1)

        entry_frame = tk.Frame(self.vocab_frame, bg="#f5f5f5")
        entry_frame.pack(fill="x", padx=4, pady=2)
        self.custom_label_var = tk.StringVar(value="")
        self.custom_label_entry = tk.Entry(entry_frame, textvariable=self.custom_label_var, font=("Segoe UI", 9), width=14)
        self.custom_label_entry.pack(side="left", padx=2)
        apply_btn = tk.Button(
            entry_frame,
            text="Apply Word",
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
    # Template Selection & Pasted Expression Preview
    # -------------------------------------------------------------------------

    def _on_apply_selected_template(self) -> None:
        pattern = self.selected_template_var.get()
        tpl = next((t for t in self.template_manager.templates if t.pattern == pattern), None)
        if tpl:
            self.template_grid_model.apply_template_to_row(
                self.template_grid_model.cursor_row,
                tpl,
                initial_values=None,  # Guarantees empty placeholders □
            )
            self.current_preview_template = None
            self.save_tpl_btn.configure(state="disabled")
            self.render_grid()

    def _on_preview_pasted_expression(self) -> None:
        expr = self.pasted_expr_var.get().strip()
        if not expr:
            return
        try:
            tpl, initial_values = ExpressionTemplateParser.parse_pasted_expression(expr)
            self.current_preview_template = tpl
            self.template_grid_model.apply_template_to_row(
                self.template_grid_model.cursor_row,
                tpl,
                initial_values=initial_values,
            )
            # Enable optional Save Template button
            self.save_tpl_btn.configure(state="normal")
            self.render_grid()
        except ValueError as ve:
            self.result_var.set("Error")
            self.result_word_var.set(str(ve))

    def _on_save_custom_template(self) -> None:
        if self.current_preview_template:
            # 1. Save immutable template structure (pattern, slot metadata) without runtime values
            clean_template = MathTemplate(
                template_id=self.current_preview_template.template_id,
                pattern=self.current_preview_template.pattern,
                name=self.current_preview_template.name,
                is_custom=True,
            )
            self.template_manager.save_custom_template(clean_template)

            # 2. Update dropdown values and select newly saved template
            self.template_patterns = [t.pattern for t in self.template_manager.templates]
            self.template_combo.configure(values=self.template_patterns)
            self.selected_template_var.set(clean_template.pattern)
            self.save_tpl_btn.configure(state="disabled")

            # 3. Apply clean saved template with empty editable placeholder (□) to active row
            self.template_grid_model.apply_template_to_row(
                self.template_grid_model.cursor_row,
                clean_template,
                initial_values=None,  # Reset slot value to empty placeholder □
            )
            self.current_preview_template = None
            self.render_grid()

            # 4. Notify user in inspector
            self.inspector_text.configure(state="normal")
            self.inspector_text.delete("1.0", "end")
            self.inspector_text.insert(
                "1.0",
                f"Template '{clean_template.pattern}' saved permanently to templates registry.\n"
                f"Column 1 is now ready with an empty editable placeholder (□)."
            )
            self.inspector_text.configure(state="disabled")

    def _prompt_next_row_type(self) -> None:
        """Presents explicit options for row type creation."""
        self.add_row_dialog()

    def add_row_dialog(self, row_type: RowType = RowType.ADDEND, explanation: str = "") -> int:
        idx = self.template_grid_model.add_row(row_type, explanation)
        self.grid_model.next_addend()
        self.render_grid()
        return idx

    def add_description_column(self) -> int:
        col_count = self.template_grid_model.add_description_column()
        self.render_grid()
        return col_count

    # -------------------------------------------------------------------------
    # Keypad & Selection Handling
    # -------------------------------------------------------------------------

    def select_cell(self, row_idx: int, area: str = "addend", col_idx: int = 0, subcol_idx: int = 0) -> None:
        self.grid_model.select_cell(row_idx, area, col_idx, subcol_idx)
        if area == "addend":
            self.template_grid_model.select_slot(row_idx, subcol_idx)
        else:
            self.template_grid_model.select_col(row_idx, col_idx + 2)
        self.render_grid()

    def delete_selected_column(self) -> None:
        self.grid_model.delete_selected_column()
        self.render_grid()

    def _on_keypad_press(self, val: str) -> None:
        if val == "=":
            self.calculate()
        elif val == "C":
            self.clear()
        elif val == "Backspace":
            self.template_grid_model.backspace()
            self.grid_model.backspace()
            self.render_grid()
        elif val in ("Next Slot (→)", "Next Subcol (→)"):
            self.grid_model.next_subcolumn()
            row = self.template_grid_model.rows[self.template_grid_model.cursor_row]
            if row.template_instance and row.template_instance.slots:
                next_s = (self.template_grid_model.cursor_slot + 1) % len(row.template_instance.slots)
                self.template_grid_model.cursor_slot = next_s
            self.render_grid()
        elif val == "Next Col (⇒)":
            self.grid_model.next_column()
            self.template_grid_model.cursor_col += 1
            self.render_grid()
        elif val == "Next Addend (↓)":
            self.add_row_dialog(RowType.ADDEND)
        elif val in ("(", ")"):
            # Parentheses define structural templates, not numeric slot contents
            if self.template_grid_model.cursor_col == 1:
                self.inspector_text.configure(state="normal")
                self.inspector_text.delete("1.0", "end")
                self.inspector_text.insert(
                    "1.0",
                    f"Notice: Parentheses '{val}' define mathematical template structure.\n\n"
                    f"Each box (□) holds a single number. To use parentheses in your math,\n"
                    f"select a parenthesized template (e.g. '(□ + □)' or '(□ + □) + □')\n"
                    f"from the Templates dropdown or enter a parenthesized expression in\n"
                    f"the 'Preview Pasted' box."
                )
                self.inspector_text.configure(state="disabled")
            else:
                self.grid_model.input_value(val)
                self.render_grid()
        elif val == "+":
            # Operator '+' is a fixed structural symbol in the mathematical template.
            # It must NOT automatically advance from a number slot into the next slot or Col 2.
            # Slot selection remains strictly explicit via direct clicking or the Next Slot button.
            if self.template_grid_model.cursor_col == 1:
                self.inspector_text.configure(state="normal")
                self.inspector_text.delete("1.0", "end")
                self.inspector_text.insert(
                    "1.0",
                    "Notice: The '+' operator is a fixed structural symbol in the mathematical template.\n\n"
                    "It does not automatically advance slots or modify numeric values.\n"
                    "To move to another slot or column, click the cell directly or use the 'Next Slot (→)' button."
                )
                self.inspector_text.configure(state="disabled")
            self.grid_model.input_value("+")
            self.render_grid()
        else:
            # Inputs numeric digit (0-9, .) into active slot or cell
            self.template_grid_model.input_number(val)
            self.grid_model.input_value(val)
            self.render_grid()

    def _on_vocab_click(self, val: str, token_type: Optional[TokenType] = None) -> None:
        tt = token_type if token_type is not None else TokenType.ITEM
        self.grid_model.input_value(val, tt)
        self.template_grid_model.set_active_value(val)
        self.render_grid()

    def _set_active_word(self, val: str) -> None:
        self._on_vocab_click(val, TokenType.ITEM)

    def _on_apply_custom_label(self) -> None:
        lbl = self.custom_label_var.get().strip()
        if lbl:
            self._set_active_word(lbl)
            self.custom_label_var.set("")

    def add_label_row(self, text: str = "Descriptive Annotation") -> int:
        idx = self.template_grid_model.add_row(RowType.LABEL, text)
        self.grid_model.add_label_row(text)
        self.render_grid()
        return idx

    # -------------------------------------------------------------------------
    # Clean Display Grid Rendering (CLICKABLE BUTTON-LIKE CELLS)
    # -------------------------------------------------------------------------

    def render_grid(self) -> None:
        for child in self.grid_frame.winfo_children():
            child.destroy()

        t_row_idx = self.template_grid_model.cursor_row
        t_col = self.template_grid_model.cursor_col
        t_slot = self.template_grid_model.cursor_slot

        # Status label
        if self.grid_model.cursor_area == "addend":
            r_idx = self.grid_model.cursor_row
            c_idx = self.grid_model.cursor_addend_col
            s_idx = self.grid_model.cursor_subcol
            val = ""
            if 0 <= r_idx < len(self.grid_model.rows):
                r = self.grid_model.rows[r_idx]
                if 0 <= c_idx < len(r.addend_columns):
                    ac = r.addend_columns[c_idx]
                    if 0 <= s_idx < len(ac.ordered_subcolumns):
                        val = ac.ordered_subcolumns[s_idx].value
            if not val and 0 <= r_idx < len(self.template_grid_model.rows):
                t_row = self.template_grid_model.rows[r_idx]
                if t_row.template_instance and s_idx < len(t_row.template_instance.slots):
                    val = t_row.template_instance.slots[s_idx].value
            status_info = f"Row {r_idx + 1} | Main Col {c_idx + 1} | Subcol {s_idx + 1} ('{val}')"
        else:
            status_info = f"Row {t_row_idx + 1}"
            if t_row_idx < len(self.template_grid_model.rows):
                cur_r = self.template_grid_model.rows[t_row_idx]
                if cur_r.row_type == RowType.LABEL:
                    status_info += " [Label Row]"
                elif t_col == 1:
                    pat = cur_r.template_instance.template.pattern if cur_r.template_instance else "math"
                    val = cur_r.template_instance.slots[t_slot].value if cur_r.template_instance and t_slot < len(cur_r.template_instance.slots) else ""
                    status_info += f" | Main Col 1 (Template: {pat}) | Subcol {t_slot + 1} ('{val}')"
                else:
                    desc_val = cur_r.description_columns[t_col - 2] if t_col - 2 < len(cur_r.description_columns) else ""
                    status_info += f" | Col {t_col} (Description: '{desc_val}')"

        self.selection_status_var.set(f"Selected Target: {status_info}")

        max_desc_cols = self.template_grid_model.get_max_description_columns()

        # Synchronize column widths across all rows and header bar so long expressions
        # or long labels never cause horizontal displacement of Columns 2 and 3.
        col0_sync_w = 140

        def _est_col1_width(row: TemplateRow) -> int:
            if row.row_type != RowType.ADDEND or not row.template_instance:
                return 320
            inst = row.template_instance
            slots_cnt = len(inst.slots)
            chars_cnt = sum(max(len(s.value) if s.value else 1, 1) for s in inst.slots)
            non_slot_chars = len(inst.template.pattern.replace("□", "").strip())
            ops_cnt = max(sum(1 for ch in inst.template.pattern if ch in ("(", ")", "+")), non_slot_chars)
            est = chars_cnt * 14 + slots_cnt * 26 + ops_cnt * 22 + 40
            return max(320, est)

        col1_sync_w = max(
            max((_est_col1_width(r) for r in self.template_grid_model.rows), default=320),
            320,
        )

        col2_sync_w = max(
            max(
                (len(r.description_columns[0]) * 10 + 36 for r in self.template_grid_model.rows if r.description_columns),
                default=140,
            ),
            140,
        )

        col3_sync_w = max(
            max(
                (len(r.description_columns[1]) * 10 + 36 for r in self.template_grid_model.rows if len(r.description_columns) > 1),
                default=180,
            ),
            180,
        )

        extra_desc_sync_w: Dict[int, int] = {}
        for i in range(2, max_desc_cols):
            col_num = i + 2
            w = max(
                max(
                    (len(r.description_columns[i]) * 10 + 36 for r in self.template_grid_model.rows if len(r.description_columns) > i),
                    default=140,
                ),
                140,
            )
            extra_desc_sync_w[col_num] = w

        self.total_grid_content_width = (
            col0_sync_w + col1_sync_w + col2_sync_w + col3_sync_w + sum(extra_desc_sync_w.values()) + 60
        )

        # Update canvas window width to accommodate synchronized width
        if hasattr(self, "canvas") and hasattr(self, "canvas_window_id"):
            cur_canvas_w = self.canvas.winfo_width()
            target_w = max(cur_canvas_w, self.total_grid_content_width)
            self.canvas.itemconfig(self.canvas_window_id, width=target_w)

        # Grid Header Bar
        header_bar = tk.Frame(self.grid_frame, bg="#e0e0e0", bd=1, relief="ridge")
        header_bar.pack(fill="x", padx=4, pady=2)
        header_bar.columnconfigure(0, weight=0, minsize=col0_sync_w)
        header_bar.columnconfigure(1, weight=0, minsize=col1_sync_w)
        header_bar.columnconfigure(2, weight=0, minsize=col2_sync_w)
        header_bar.columnconfigure(3, weight=0, minsize=col3_sync_w)
        for col_num, w in extra_desc_sync_w.items():
            header_bar.columnconfigure(col_num, weight=0, minsize=w)

        tk.Label(header_bar, text="Row", font=("Segoe UI", 9, "bold"), bg="#e0e0e0", anchor="w", padx=6).grid(row=0, column=0, sticky="w")
        tk.Label(
            header_bar,
            text="Column 1: Mathematical Template (Editable Slots □)",
            font=("Segoe UI", 9, "bold"),
            fg="#1b5e20",
            bg="#e0e0e0",
            anchor="w",
            padx=6,
        ).grid(row=0, column=1, sticky="w")
        tk.Label(
            header_bar,
            text="Column 2: Item",
            font=("Segoe UI", 9, "bold"),
            fg="#6a1b9a",
            bg="#e0e0e0",
            anchor="w",
            padx=6,
        ).grid(row=0, column=2, sticky="w")
        tk.Label(
            header_bar,
            text="Column 3: Context",
            font=("Segoe UI", 9, "bold"),
            fg="#6a1b9a",
            bg="#e0e0e0",
            anchor="w",
            padx=6,
        ).grid(row=0, column=3, sticky="w")
        for col_num in sorted(extra_desc_sync_w.keys()):
            tk.Label(
                header_bar,
                text=f"Column {col_num}: Extra Desc",
                font=("Segoe UI", 9, "bold"),
                fg="#6a1b9a",
                bg="#e0e0e0",
                anchor="w",
                padx=6,
            ).grid(row=0, column=col_num, sticky="w")

        # Render rows
        for r_idx, row in enumerate(self.template_grid_model.rows):
            is_active_row = (r_idx == t_row_idx)
            row_bg = "#fffde7" if is_active_row else "#ffffff"

            row_card = tk.Frame(self.grid_frame, bg=row_bg, bd=2 if is_active_row else 1, relief="solid" if is_active_row else "ridge")
            row_card.pack(fill="x", expand=True, padx=4, pady=3)
            row_card.columnconfigure(0, weight=0, minsize=col0_sync_w)
            row_card.columnconfigure(1, weight=0, minsize=col1_sync_w)
            row_card.columnconfigure(2, weight=0, minsize=col2_sync_w)
            row_card.columnconfigure(3, weight=0, minsize=col3_sync_w)
            for col_num, w in extra_desc_sync_w.items():
                row_card.columnconfigure(col_num, weight=0, minsize=w)

            # Row Tag
            if row.row_type == RowType.LABEL:
                tag_lbl = tk.Label(
                    row_card,
                    text=f"[Label Row {r_idx + 1}]",
                    font=("Segoe UI", 9, "bold"),
                    bg="#ede7f6",
                    fg="#4a148c",
                    width=14,
                    anchor="w",
                    padx=6,
                    cursor="hand2",
                )
                tag_lbl.grid(row=0, column=0, sticky="w", padx=4, pady=4)
                tag_lbl.bind("<Button-1>", lambda _e, r=r_idx: self.select_cell(r, "label", 0, 0))

                lbl_val = tk.Label(
                    row_card,
                    text=row.explanation_text or "(Click to edit description row)",
                    font=("Segoe UI", 10, "italic"),
                    bg=row_bg,
                    fg="#333333",
                    anchor="w",
                    padx=8,
                    cursor="hand2",
                )
                lbl_val.grid(row=0, column=1, columnspan=max(1, max_desc_cols + 1), sticky="w", padx=4, pady=4)
                lbl_val.bind("<Button-1>", lambda _e, r=r_idx: self.select_cell(r, "label", 0, 0))
                continue

            # Addend Row
            tag_text = f"Row {r_idx + 1} (Addend)" if r_idx == 0 else f"Row {r_idx + 1} (Addend +)"
            tag_lbl = tk.Label(
                row_card,
                text=tag_text,
                font=("Segoe UI", 9, "bold"),
                bg="#e8f5e9" if not is_active_row else "#c8e6c9",
                fg="#1b5e20",
                width=14,
                anchor="w",
                padx=6,
                cursor="hand2",
            )
            tag_lbl.grid(row=0, column=0, sticky="w", padx=4, pady=4)
            tag_lbl.bind("<Button-1>", lambda _e, r=r_idx: self.select_cell(r, "addend", 0, 0))

            # Column 1: Mathematical Template with Editable Slots
            col1_frame = tk.Frame(row_card, bg="#fafafa", bd=1, relief="groove")
            col1_frame.grid(row=0, column=1, sticky="w", padx=4, pady=4)

            if row.template_instance:
                self._render_template_instance_col1(col1_frame, r_idx, row.template_instance, is_active_row)

            # Columns 2, 3, and beyond: Descriptive Columns
            for d_idx, desc_val in enumerate(row.description_columns):
                col_number = d_idx + 2
                is_active_col = (is_active_row and t_col == col_number)

                desc_cell = tk.Label(
                    row_card,
                    text=desc_val or f"[ Col {col_number} ]",
                    font=("Segoe UI", 9, "bold" if desc_val else "italic"),
                    fg="#4a148c" if desc_val else "#999999",
                    bg="#fff59d" if is_active_col else "#ffffff",
                    bd=2 if is_active_col else 1,
                    relief="solid" if is_active_col else "ridge",
                    cursor="hand2",
                    anchor="w",
                    padx=8,
                    pady=3,
                )
                desc_cell.grid(row=0, column=col_number, sticky="ew", padx=4, pady=4)
                desc_cell.bind("<Button-1>", lambda _e, r=r_idx, c=col_number: self.template_grid_model.select_col(r, c) or self.render_grid())

    def _render_template_instance_col1(
        self,
        parent: tk.Widget,
        row_idx: int,
        inst: TemplateInstance,
        is_active_row: bool
    ) -> None:
        """Renders mathematical template pattern with clickable, button-like slot cells."""
        pattern = inst.template.pattern
        slot_idx = 0
        i = 0
        while i < len(pattern):
            ch = pattern[i]
            if ch == "□":
                if slot_idx < len(inst.slots):
                    slot = inst.slots[slot_idx]
                    is_active_slot = (
                        is_active_row and
                        self.template_grid_model.cursor_col == 1 and
                        self.template_grid_model.cursor_slot == slot_idx
                    )
                    slot_txt = slot.value if slot.value else "□"
                    slot_btn = tk.Label(
                        parent,
                        text=f" {slot_txt} ",
                        font=("Segoe UI", 10, "bold"),
                        bg="#fff59d" if is_active_slot else "#e8f5e9",
                        fg="#b71c1c" if is_active_slot else "#1b5e20",
                        bd=2 if is_active_slot else 1,
                        relief="solid" if is_active_slot else "raised",
                        cursor="hand2",
                        padx=4,
                        pady=2,
                    )
                    slot_btn.pack(side="left", padx=2, pady=2)
                    slot_btn.bind("<Button-1>", lambda _e, r=row_idx, s=slot_idx: self._select_template_slot(r, s))
                    slot_idx += 1
                i += 1
            elif ch in ("(", ")", "+"):
                sym_lbl = tk.Label(
                    parent,
                    text=ch,
                    font=("Segoe UI", 10, "bold"),
                    fg="#0d47a1" if ch in ("(", ")") else "#e65100",
                    bg="#fafafa",
                    padx=2,
                )
                sym_lbl.pack(side="left")
                i += 1
            elif ch.isspace():
                i += 1
            else:
                i += 1

    def _select_template_slot(self, r: int, s: int) -> None:
        self.template_grid_model.select_slot(r, s)
        self.grid_model.select_cell(r, "addend", 0, s)
        self.render_grid()

    # -------------------------------------------------------------------------
    # Calculation & Safe Exception Boundary
    # -------------------------------------------------------------------------

    def calculate(self) -> Optional[ParseResult]:
        """Calculates result across rows safely catching validation errors."""
        try:
            # First try template-driven calculation if template slots are filled
            template_rows_filled = any(
                r.row_type == RowType.ADDEND and r.template_instance and any(s.is_filled for s in r.template_instance.slots)
                for r in self.template_grid_model.rows
            )
            if template_rows_filled:
                parse_res = self.template_grid_model.calculate()
            else:
                parse_res = self.grid_model.calculate()

        except ValueError as ve:
            err_msg = str(ve)
            self.last_parse_result = None
            self.result_var.set("Error")
            self.result_word_var.set(err_msg)

            # Update Dedicated Results Text Window
            self.results_text.configure(state="normal")
            self.results_text.delete("1.0", "end")
            self.results_text.insert(
                "1.0",
                f"╔══════════════════════════════════════════════════════════════════════════════\n"
                f"║ VALIDATION NOTICE: Calculation Not Completed\n"
                f"╚══════════════════════════════════════════════════════════════════════════════\n\n"
                f"Error Details:\n  {err_msg}\n\n"
                f"Action Required:\n"
                f"  1. Review the highlighted incomplete slot (□) or description column.\n"
                f"  2. Use the central keypad or label console to fill the required value.\n"
                f"  3. Press '=' or Calculate again.\n\n"
                f"Note: All current cell inputs and templates remain intact."
            )
            self.results_text.configure(state="disabled")

            # Update Inspector
            self.inspector_text.configure(state="normal")
            self.inspector_text.delete("1.0", "end")
            self.inspector_text.insert(
                "1.0",
                f"Validation Error: {err_msg}\n\n"
                f"Action Required:\n"
                f"1. Click the incomplete slot (□) or description column.\n"
                f"2. Use the central keypad or label console to fill the required value.\n"
                f"3. Press '=' or Calculate again.\n\n"
                f"All existing cell values remain intact."
            )
            self.inspector_text.configure(state="disabled")
            self.render_grid()
            return None
        except Exception as e:
            err_msg = str(e)
            self.last_parse_result = None
            self.result_var.set("Error")
            self.result_word_var.set(err_msg)

            self.results_text.configure(state="normal")
            self.results_text.delete("1.0", "end")
            self.results_text.insert(
                "1.0",
                f"╔══════════════════════════════════════════════════════════════════════════════\n"
                f"║ CALCULATION ERROR\n"
                f"╚══════════════════════════════════════════════════════════════════════════════\n\n"
                f"Error Details:\n  {err_msg}"
            )
            self.results_text.configure(state="disabled")

            self.inspector_text.configure(state="normal")
            self.inspector_text.delete("1.0", "end")
            self.inspector_text.insert("1.0", f"Calculation Error:\n{err_msg}")
            self.inspector_text.configure(state="disabled")
            self.render_grid()
            return None

        self.last_parse_result = parse_res

        if not parse_res:
            self.result_var.set("")
            self.result_word_var.set("Expression is empty")
            self.results_text.configure(state="normal")
            self.results_text.delete("1.0", "end")
            self.results_text.insert("1.0", "Expression is empty.")
            self.results_text.configure(state="disabled")
            return None

        # Exact Decimal representation preserved
        self.result_var.set(parse_res.total_number)
        self.result_word_var.set(parse_res.word_result)

        # Update Dedicated Results Text Window
        self.results_text.configure(state="normal")
        self.results_text.delete("1.0", "end")

        result_lines = [
            "╔══════════════════════════════════════════════════════════════════════════════",
            f"║ NUMERICAL TOTAL:    {parse_res.total_number}",
            f"║ DESCRIPTIVE RESULT: {parse_res.word_result}",
            "╚══════════════════════════════════════════════════════════════════════════════",
            "",
            "─── MATHEMATICAL ADDEND BREAKDOWN ───",
        ]
        for term in parse_res.individual_terms:
            ctx = f" ({term.context})" if term.context else ""
            result_lines.append(f"  • Quantity: {term.quantity} {term.item}{ctx}")

        if parse_res.aggregated_terms:
            result_lines.append("")
            result_lines.append("─── AGGREGATED CATEGORIES ───")
            for term in parse_res.aggregated_terms:
                ctx = f" ({term.context})" if term.context else ""
                result_lines.append(f"  • Subtotal: {term.quantity} {term.item}{ctx}")

        self.results_text.insert("1.0", "\n".join(result_lines))
        self.results_text.configure(state="disabled")

        # Update Inspector
        self.inspector_text.configure(state="normal")
        self.inspector_text.delete("1.0", "end")

        output_lines = [
            f"=== TOTAL SUMMARY ===",
            f"Math Total: {parse_res.total_number}",
            f"Sentence Result: {parse_res.word_result}",
            f"\n=== ADDEND REPRESENTATIONS ===",
        ]

        has_grid_tokens = any(
            any(ac.ordered_subcolumns for ac in r.addend_columns)
            for r in self.grid_model.rows if r.row_type == RowType.ADDEND
        )
        if has_grid_tokens:
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
        else:
            for r_idx, row in enumerate(self.template_grid_model.rows):
                if row.row_type != RowType.ADDEND:
                    output_lines.append(f"\n[Row {r_idx + 1}: Label Row] — '{row.explanation_text}'")
                    continue

                inst = row.template_instance
                pat = inst.template.pattern if inst else "empty"
                output_lines.append(f"\n--- Row {r_idx + 1}: Template ({pat}) ---")
                if inst:
                    for s in inst.slots:
                        output_lines.append(f"  Field '{s.name}': {s.value or '□'}")
                output_lines.append(f"  Item (Col 2): '{row.description_columns[0]}'")
                output_lines.append(f"  Context (Col 3): '{row.description_columns[1]}'")

                # Rep 1, Rep 2, Rep 3 for template instances
                raw_toks = inst.to_token_stream(row.description_columns) if inst else []
                subcol_str = " | ".join(f"'{t.value}'" for t in raw_toks)
                output_lines.append(f"  Rep 1 (Ordered Subcolumns): [{subcol_str}]")
                output_lines.append(f"  Rep 2 (Parsed Structure - Unaggregated):")
                for t in parse_res.individual_terms:
                    ctx = f", context='{t.context}'" if t.context else ""
                    output_lines.append(f"    Quantity: {t.quantity}, Unit: '{t.item}'{ctx}")
                output_lines.append(f"  Rep 3 (Aggregated Results by Units):")
                for t in parse_res.aggregated_terms:
                    ctx = f" {t.context}" if t.context else ""
                    output_lines.append(f"    Subtotal: {t.quantity} {t.item}{ctx}")

        self.inspector_text.insert("1.0", "\n".join(output_lines))
        self.inspector_text.configure(state="disabled")

        self.render_grid()
        return parse_res

    def clear(self) -> None:
        self.template_grid_model.clear()
        self.grid_model.clear()
        self.last_parse_result = None
        self.result_var.set("")
        self.result_word_var.set("")

        self.results_text.configure(state="normal")
        self.results_text.delete("1.0", "end")
        self.results_text.insert("1.0", "Cleared. Ready for new calculation.")
        self.results_text.configure(state="disabled")

        self.inspector_text.configure(state="normal")
        self.inspector_text.delete("1.0", "end")
        self.inspector_text.insert("1.0", "Cleared.")
        self.inspector_text.configure(state="disabled")

        self.render_grid()

    def run(self) -> None:
        """Runs Tkinter mainloop catching only KeyboardInterrupt for clean termination."""
        if self._owns_root:
            try:
                self.root.mainloop()
            except KeyboardInterrupt:
                try:
                    self.root.destroy()
                except Exception:
                    pass


def main() -> None:
    """Application entry point catching only KeyboardInterrupt for graceful exit."""
    try:
        app = AdditionTokenCalculator()
        app.run()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
