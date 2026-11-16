"""Builds an operator as a row of cards (blue +, 3x3 arrows, [Item], [Context], orange +).

A card whose centre is the small box  □  is a number card (blue centre).  A card whose centre is
text (+, sin(, ∫ ...) is an operator card (yellow centre, same shape as the helper card).

A row is   LEFT cards  =  RIGHT cards.
  stacked=False  -> the full operator row, e.g.   [□] [+] [□]  =  [□]
  stacked=True   -> only the operator itself, e.g.  [+]  =  [□]
                    (the operands come from the rows above, which is how rows get stacked)
The result card on the right of "=" is the number card of Row 1 in the main window.
Nothing here calculates yet.
"""
import os
import sys
import tkinter as tk

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gui_coordinates import (
    EXCEL_13COL_MATH_BOX1,
    EXCEL_13COL_MATH_TRAILING,
    EXCEL_13COL_RESULT_BOX1,
    EXCEL_13COL_RESULT_TRAILING,
    excel_13col_start_row,
    EXCEL_17COL_MATH_BOX1,
    EXCEL_17COL_MATH_TRAILING,
    EXCEL_17COL_RESULT_BOX1,
    EXCEL_17COL_RESULT_TRAILING,
    excel_17col_start_row,
)
from gui_style import (ARROW_BG, ARROW_GRID_POSITIONS, ARROWS, BLUE, GridPosition, LayoutRegion,  # noqa: E402
                       CARD_COMPONENT_POSITIONS, CREAM, PALE_BLUE, PALE_ORANGE,
                       btn, CARD_9COL_LEAD_BUTTON_POS, CARD_9COL_ARROW_GRID_POS,
                       CARD_9COL_CENTER_POS, CARD_9COL_LABEL_POS,
                       CARD_9COL_CONTEXT_POS, CARD_9COL_TRAILING_BUTTON_POS,
                       CARD_9COL_ARROW_POSITIONS, CARD_CENTER_POSITION,
                       card_to_excel_position)

BOX = "□"


import math
import tkinter.font as tkfont


def word_entry(parent, hint, value, width=10, on_change=None, on_focus=None):
    """A box that takes typed words and dynamically auto-expands to the right to fit all text."""
    e = tk.Entry(parent, font=("Segoe UI", 12), width=width, relief="solid", bd=1, justify="center")
    e.hinted = False
    min_width = max(width, 10)

    def update_entry_width():
        txt = e.get()
        if not txt:
            e.configure(width=min_width)
            return
        f = tkfont.Font(font=e.cget("font"))
        char_w = max(f.measure("0"), 1)
        needed_chars = int(math.ceil(f.measure(txt) / char_w)) + 3
        e.configure(width=max(needed_chars, min_width))

    def show_hint():
        e.delete(0, "end")
        e.insert(0, hint)
        e.configure(fg="#999999")
        e.hinted = True
        update_entry_width()

    def text():
        return "" if e.hinted else e.get()

    def focus_in(_event=None):
        if e.hinted:
            e.delete(0, "end")
            e.configure(fg="black")
            e.hinted = False
            update_entry_width()
        if on_focus:
            on_focus()

    def focus_out(_event=None):
        if not e.get():
            show_hint()
        else:
            update_entry_width()

    def set_text(val):
        e.delete(0, "end")
        if val:
            e.insert(0, val)
            e.configure(fg="black")
            e.hinted = False
        else:
            show_hint()
        update_entry_width()
        if on_change:
            on_change(text())

    def on_key(_event=None):
        update_entry_width()
        if on_change:
            on_change(text())

    if value:
        e.insert(0, value)
        update_entry_width()
    else:
        show_hint()

    e.bind("<FocusIn>", focus_in)
    e.bind("<FocusOut>", focus_out)
    e.bind("<KeyRelease>", on_key)
    e.words_text = text
    e.set_text = set_text
    e.show_hint = show_hint
    e.update_entry_width = update_entry_width
    return e


class DescriptionRegion(tk.Frame):
    """Authoritative layout region for descriptive text boxes in 13-column or 17-column Excel grid.

    Occupies Columns F..G (Math) or L..M / P..Q (Result).
    Initially holds Box 1 and Orange + button.
    Auto-expands rightward as text is typed without moving Box 1's left edge.
    Clicking orange + adds Box 2, Box 3, etc. to the right, pushing orange + right.
    """
    def __init__(self, parent, role="math", calc_row=1, words=None, num_boxes=1,
                 on_words=None, on_focus=None, on_add_box=None, use_17col=True, **kwargs):
        super().__init__(parent, bg=CREAM, **kwargs)
        self.role = role  # "math" or "result"
        self.calc_row = calc_row
        self.use_17col = use_17col
        self.on_words_cb = on_words
        self.on_focus_cb = on_focus
        self.on_add_box_cb = on_add_box

        # Track text data
        if words is None:
            raw_words = []
        elif isinstance(words, (list, tuple)):
            raw_words = list(words)
        else:
            raw_words = [str(words)]
        self.words_data = list(raw_words)
        while len(self.words_data) < 1:
            self.words_data.append("")

        self.num_boxes = max(1, int(num_boxes) if num_boxes is not None else len(raw_words))
        while len(self.words_data) < self.num_boxes:
            self.words_data.append("")

        self.boxes = []
        self._box1 = None
        self._box2 = None

        if self.use_17col:
            col_trailing = EXCEL_17COL_MATH_TRAILING if role == "math" else EXCEL_17COL_RESULT_TRAILING
            r0 = excel_17col_start_row(calc_row)
        else:
            col_trailing = EXCEL_13COL_MATH_TRAILING if role == "math" else EXCEL_13COL_RESULT_TRAILING
            r0 = excel_13col_start_row(calc_row)

        self.trailing_btn = btn(self, "+", PALE_ORANGE, fg="#c07000",
                                font=("Segoe UI", 14, "bold"), width=3,
                                highlightbackground="#e0a060", command=self.add_box)
        self.trailing_btn.grid_pos = GridPosition(row=r0 + 1, column=col_trailing, region=LayoutRegion.EXCEL_WORKSPACE)
        self.trailing_btn.excel_pos = self.trailing_btn.grid_pos

        # Create initial boxes
        for i in range(self.num_boxes):
            self._create_box_widget(i)

        self.trailing_btn.pack(side="left", padx=1, pady=2)

    def _create_box_widget(self, idx: int):
        if self.use_17col:
            col_box1 = EXCEL_17COL_MATH_BOX1 if self.role == "math" else EXCEL_17COL_RESULT_BOX1
            r0 = excel_17col_start_row(self.calc_row)
        else:
            col_box1 = EXCEL_13COL_MATH_BOX1 if self.role == "math" else EXCEL_13COL_RESULT_BOX1
            r0 = excel_13col_start_row(self.calc_row)
        hint = f"Descriptive Text Box {idx + 1}"
        val = self.words_data[idx] if idx < len(self.words_data) else ""
        b = word_entry(self, hint, val, width=10,
                       on_change=lambda t, i=idx: self._on_box_change(i, t),
                       on_focus=lambda i=idx: self._on_box_focus(i))
        card_col = col_box1 if idx == 0 else col_box1 + idx
        b.grid_pos = GridPosition(row=r0 + 1, column=card_col, region=LayoutRegion.EXCEL_WORKSPACE)
        b.excel_pos = b.grid_pos
        b.pack(side="left", padx=1, pady=2)
        self.boxes.append(b)
        if idx == 0:
            self._box1 = b
        elif idx == 1:
            self._box2 = b
        return b

    def add_box(self):
        """Add next descriptive box, push orange + to the right."""
        for i, b in enumerate(self.boxes):
            if hasattr(b, "words_text"):
                self.words_data[i] = b.words_text()
            else:
                self.words_data[i] = b.get()

        new_idx = len(self.boxes)
        self.num_boxes = new_idx + 1
        while len(self.words_data) < self.num_boxes:
            self.words_data.append("")

        self.trailing_btn.pack_forget()
        b = self._create_box_widget(new_idx)
        if self.use_17col:
            col_trailing = EXCEL_17COL_MATH_TRAILING if self.role == "math" else EXCEL_17COL_RESULT_TRAILING
            r0 = excel_17col_start_row(self.calc_row)
        else:
            col_trailing = EXCEL_13COL_MATH_TRAILING if self.role == "math" else EXCEL_13COL_RESULT_TRAILING
            r0 = excel_13col_start_row(self.calc_row)
        trailing_col = col_trailing if self.num_boxes == 1 else col_trailing + (self.num_boxes - 1)
        self.trailing_btn.grid_pos = GridPosition(row=r0 + 1, column=trailing_col, region=LayoutRegion.EXCEL_WORKSPACE)
        self.trailing_btn.excel_pos = self.trailing_btn.grid_pos
        self.trailing_btn.pack(side="left", padx=1, pady=2)

        try:
            b.focus_set()
        except Exception:
            pass

        if self.on_add_box_cb:
            self.on_add_box_cb(self.num_boxes)
        return b

    @property
    def box1(self):
        return self.boxes[0] if self.boxes else self._box1

    @property
    def box2(self):
        return self.boxes[1] if len(self.boxes) >= 2 else None

    def _flush_active_extra_text(self):
        for i, b in enumerate(self.boxes):
            if hasattr(b, "words_text"):
                self.words_data[i] = b.words_text()
            else:
                self.words_data[i] = b.get()

    def _on_box_change(self, idx, text):
        while len(self.words_data) <= idx:
            self.words_data.append("")
        self.words_data[idx] = text
        if self.on_words_cb:
            self.on_words_cb(idx, text)

    def _on_box_focus(self, idx):
        if self.on_focus_cb:
            self.on_focus_cb(idx)

    def reset(self):
        """Reset description region to exactly 1 empty box and restore default orange + position."""
        for b in self.boxes[1:]:
            try:
                b.destroy()
            except Exception:
                pass
        self.boxes = self.boxes[:1]
        self._box2 = None
        self.num_boxes = 1
        self.words_data = [""]
        if self.boxes:
            b0 = self.boxes[0]
            if hasattr(b0, "set_text"):
                b0.set_text("")
            elif hasattr(b0, "delete"):
                b0.delete(0, "end")
        if self.use_17col:
            col_trailing = EXCEL_17COL_MATH_TRAILING if self.role == "math" else EXCEL_17COL_RESULT_TRAILING
            r0 = excel_17col_start_row(self.calc_row)
        else:
            col_trailing = EXCEL_13COL_MATH_TRAILING if self.role == "math" else EXCEL_13COL_RESULT_TRAILING
            r0 = excel_13col_start_row(self.calc_row)
        self.trailing_btn.pack_forget()
        self.trailing_btn.grid_pos = GridPosition(row=r0 + 1, column=col_trailing, region=LayoutRegion.EXCEL_WORKSPACE)
        self.trailing_btn.excel_pos = self.trailing_btn.grid_pos
        self.trailing_btn.pack(side="left", padx=1, pady=2)
        if self.on_add_box_cb:
            self.on_add_box_cb(1)
        if self.on_words_cb:
            self.on_words_cb(0, "")

    def get_words(self):
        self._flush_active_extra_text()
        return tuple(self.words_data[:len(self.boxes)])

    def to_excel_coordinate(self, widget_or_pos):
        return getattr(widget_or_pos, "excel_pos", getattr(widget_or_pos, "grid_pos", widget_or_pos))

    @property
    def box1(self):
        return self.boxes[0] if self.boxes else self._box1

    @property
    def box2(self):
        return self.boxes[1] if len(self.boxes) >= 2 else None

    @property
    def label_widget(self):
        return self.box1

    @property
    def context_widget(self):
        return self.box2

    @property
    def label_box(self):
        return self.box1

    @property
    def context_box(self):
        if self.num_boxes < 2:
            self.add_box()
        return self.box2


class CardFrame(tk.Frame):
    """Authoritative 9-column x 3-row Excel card frame supporting dynamic descriptive text boxes."""

    def __init__(self, parent, center, kind, lead="+", on_pick=None, selected=False,
                 words=None, on_words=None, on_focus=None, card_slot=None, calc_row=1,
                 num_boxes=None, on_add_box=None, as_buttons=False, current_page=None, **kwargs):
        super().__init__(parent, bg=CREAM, **kwargs)
        if card_slot is None:
            card_slot = 3 if lead == "=" else (1 if kind == "helper" else 2)
        self.card_slot = card_slot
        self.calc_row = calc_row
        self.kind = kind
        self.on_words_cb = on_words
        self.on_focus_cb = on_focus
        self.on_add_box_cb = on_add_box
        self.as_buttons = as_buttons

        # Configure 8 columns matching my_excel_sheet.txt; column 1 is empty spacer
        self.grid_columnconfigure(0, minsize=42)   # Card col 1: Lead button
        self.grid_columnconfigure(1, minsize=10)   # Card col 2: Empty spacer 1
        self.grid_columnconfigure(2, minsize=24)   # Card col 3: Left arrow column
        self.grid_columnconfigure(3, minsize=28)   # Card col 4: Mid arrow column / Center square
        self.grid_columnconfigure(4, minsize=24)   # Card col 5: Right arrow column
        self.grid_columnconfigure(5, minsize=90)   # Card col 6: Label / Item entry (Box 1)
        self.grid_columnconfigure(6, minsize=90)   # Card col 7: Context entry (Box 2 / Pager)
        self.grid_columnconfigure(7, minsize=42)   # Card col 8: Trailing button (Orange +)

        # Row configure for 3 rows
        self.grid_rowconfigure(0, minsize=26)      # Row 1 (Top arrows)
        self.grid_rowconfigure(1, minsize=44)      # Row 2 (Middle: center square, lead, entries, trailing)
        self.grid_rowconfigure(2, minsize=26)      # Row 3 (Bottom arrows)

        # 1. Blue plus / lead button (column 1, row 2)
        pos_lead = CARD_9COL_LEAD_BUTTON_POS
        self.lead_btn = btn(self, lead, PALE_BLUE, fg=BLUE if lead == "+" else "black",
                            font=("Segoe UI", 14, "bold"), width=3,
                            highlightbackground=BLUE, command=on_pick or (lambda: None))
        self.lead_btn.grid_pos = pos_lead
        self.lead_btn.excel_pos = card_to_excel_position(pos_lead, card_slot, calc_row)
        self.lead_btn.grid(**pos_lead.to_tkinter_grid(), sticky="nsew", padx=1, pady=1)

        # 2. Directional arrow buttons & center square (columns 3..5, rows 1..3)
        self.arrow_buttons = {}
        for pos, sym in CARD_9COL_ARROW_POSITIONS.items():
            if sym:
                b = tk.Button(self, text=sym, width=2, bg=ARROW_BG, relief="groove",
                              command=lambda: None)
                b.grid_pos = pos
                b.excel_pos = card_to_excel_position(pos, card_slot, calc_row)
                b.grid(**pos.to_tkinter_grid(), sticky="nsew", padx=1, pady=1)
                self.arrow_buttons[pos] = b
            else:
                bg = "#fbd34d" if kind == "helper" else PALE_BLUE
                if selected:
                    bg = "#5b9bf0"
                self.center_btn = tk.Button(self, text=center, width=max(2, len(center) + 1), bg=bg,
                                             relief="sunken" if selected else "solid", bd=1,
                                             font=("Segoe UI", 12, "bold"), command=on_pick or (lambda: None))
                self.center_btn.grid_pos = pos
                self.center_btn.excel_pos = card_to_excel_position(pos, card_slot, calc_row)
                self.center_btn.grid(**pos.to_tkinter_grid(), sticky="nsew", padx=1, pady=1)
                self.arrow_buttons[pos] = self.center_btn

        # Backward compatibility alias
        self.grid_frame = self

        # 3. Words & Text Boxes
        pos_label = CARD_9COL_LABEL_POS
        pos_context = CARD_9COL_CONTEXT_POS

        if words is None:
            raw_words = []
        elif isinstance(words, (list, tuple)):
            raw_words = list(words)
        else:
            raw_words = [str(words)]

        self.words_data = list(raw_words)
        while len(self.words_data) < 1:
            self.words_data.append("")

        if num_boxes is not None:
            self.num_boxes = max(1, int(num_boxes))
        else:
            non_empty = sum(1 for w in raw_words if isinstance(w, str) and w.strip())
            self.num_boxes = max(1, non_empty)

        while len(self.words_data) < self.num_boxes:
            self.words_data.append("")

        self.current_page = current_page if current_page is not None else self.num_boxes
        self.boxes = []
        self._box1 = None
        self._box2 = None
        self.extra_frame = None
        self._active_extra_box = None
        self._label_btn = None
        self._context_btn = None

        if self.as_buttons:
            # Button mode: static 8-column layout
            pos_trailing = CARD_9COL_TRAILING_BUTTON_POS
            lbl_text = "[Label]" if kind == "helper" else "[Item]"
            self._label_btn = tk.Button(self, text=lbl_text, font=("Segoe UI", 12), bg="white", relief="solid", bd=1,
                                        width=7, command=lambda: None)
            self._label_btn.grid_pos = pos_label
            self._label_btn.excel_pos = card_to_excel_position(pos_label, card_slot, calc_row)
            self._label_btn.grid(**pos_label.to_tkinter_grid(), sticky="nsew", padx=2, pady=1)

            self._context_btn = tk.Button(self, text="[Context]", font=("Segoe UI", 12), bg="white", relief="solid", bd=1,
                                          width=7, command=lambda: None)
            self._context_btn.grid_pos = pos_context
            self._context_btn.excel_pos = card_to_excel_position(pos_context, card_slot, calc_row)
            self._context_btn.grid(**pos_context.to_tkinter_grid(), sticky="nsew", padx=2, pady=1)

            self.trailing_btn = btn(self, "+", PALE_ORANGE, fg="#c07000", font=("Segoe UI", 14, "bold"), width=3,
                                    highlightbackground="#e0a060", command=self.add_box)
            self.trailing_btn.grid_pos = pos_trailing
            self.trailing_btn.excel_pos = card_to_excel_position(pos_trailing, card_slot, calc_row)
            self.trailing_btn.grid(**pos_trailing.to_tkinter_grid(), sticky="nsew", padx=1, pady=1)

            self.card_controls = {
                pos_lead: self.lead_btn,
                pos_label: self._label_btn,
                pos_context: self._context_btn,
                pos_trailing: self.trailing_btn,
                self.center_btn.grid_pos: self.center_btn,
            }
        else:
            # Dynamic descriptive text boxes mode
            for i in range(self.num_boxes):
                card_col = 6 + i
                tk_col = card_col - 1
                pos_box = GridPosition(row=2, column=card_col, region=LayoutRegion.CARD_COMPONENT)
                hint = f"Descriptive Text Box {i + 1}"
                val = self.words_data[i]
                b = word_entry(self, hint, val, 7,
                               on_change=lambda t, idx=i: self._on_box_change(idx, t),
                               on_focus=lambda idx=i: self._on_box_focus(idx))
                b.grid_pos = pos_box
                b.excel_pos = card_to_excel_position(pos_box, card_slot, calc_row)
                self.grid_columnconfigure(tk_col, minsize=90)
                b.grid(row=1, column=tk_col, sticky="nsew", padx=2, pady=1)
                self.boxes.append(b)
                if i == 0:
                    self._box1 = b
                elif i == 1:
                    self._box2 = b

            trailing_card_col = 6 + self.num_boxes
            trailing_tk_col = trailing_card_col - 1
            pos_trailing = GridPosition(row=2, column=trailing_card_col, region=LayoutRegion.CARD_COMPONENT)
            self.trailing_btn = btn(self, "+", PALE_ORANGE, fg="#c07000", font=("Segoe UI", 14, "bold"), width=3,
                                    highlightbackground="#e0a060", command=self.add_box)
            self.trailing_btn.grid_pos = pos_trailing
            self.trailing_btn.excel_pos = card_to_excel_position(pos_trailing, card_slot, calc_row)
            self.grid_columnconfigure(trailing_tk_col, minsize=42)
            self.trailing_btn.grid(row=1, column=trailing_tk_col, sticky="nsew", padx=1, pady=1)

            self.card_controls = {
                pos_lead: self.lead_btn,
                self.center_btn.grid_pos: self.center_btn,
                pos_trailing: self.trailing_btn,
            }
            for b in self.boxes:
                self.card_controls[b.grid_pos] = b

        for pos, b in self.arrow_buttons.items():
            self.card_controls[pos] = b

    @property
    def label_widget(self):
        if self._label_btn is not None:
            return self._label_btn
        return self.boxes[0] if self.boxes else self._box1

    @property
    def context_widget(self):
        if self._context_btn is not None:
            return self._context_btn
        if len(self.boxes) >= 2:
            return self.boxes[1]
        return None

    @property
    def label_btn(self):
        if self._label_btn is not None:
            return self._label_btn
        return self.boxes[0] if self.boxes else self._box1

    @label_btn.setter
    def label_btn(self, val):
        self._label_btn = val

    @property
    def context_btn(self):
        if self._context_btn is not None:
            return self._context_btn
        if len(self.boxes) >= 2:
            return self.boxes[1]
        return None

    @context_btn.setter
    def context_btn(self, val):
        self._context_btn = val

    @property
    def label_box(self):
        return self.boxes[0] if self.boxes else self._box1

    @label_box.setter
    def label_box(self, val):
        self._box1 = val

    @property
    def context_box(self):
        if self.as_buttons:
            return None
        if self.num_boxes < 2:
            self.add_box()
        if len(self.boxes) >= 2:
            try:
                self.boxes[1].update_idletasks()
            except Exception:
                pass
            return self.boxes[1]
        return None

    @context_box.setter
    def context_box(self, val):
        if len(self.boxes) >= 2:
            self.boxes[1] = val

    @property
    def box1(self):
        return self.boxes[0] if self.boxes else self._box1

    @property
    def box2(self):
        if len(self.boxes) >= 2:
            return self.boxes[1]
        return None

    def _render_extra_frame(self):
        pass

    def add_box(self):
        """Add the next descriptive text box and push the orange + button to the right."""
        if self.as_buttons:
            return
        for i, b in enumerate(self.boxes):
            if hasattr(b, "words_text"):
                self.words_data[i] = b.words_text()
            else:
                self.words_data[i] = b.get()

        new_idx = len(self.boxes)
        self.num_boxes = new_idx + 1
        while len(self.words_data) < self.num_boxes:
            self.words_data.append("")

        card_col = 6 + new_idx
        tk_col = card_col - 1
        pos_new = GridPosition(row=2, column=card_col, region=LayoutRegion.CARD_COMPONENT)
        hint = f"Descriptive Text Box {new_idx + 1}"
        val = self.words_data[new_idx]

        b = word_entry(self, hint, val, 7,
                       on_change=lambda t, idx=new_idx: self._on_box_change(idx, t),
                       on_focus=lambda idx=new_idx: self._on_box_focus(idx))
        b.grid_pos = pos_new
        b.excel_pos = card_to_excel_position(pos_new, self.card_slot, self.calc_row)
        self.grid_columnconfigure(tk_col, minsize=90)
        b.grid(row=1, column=tk_col, sticky="nsew", padx=2, pady=1)
        self.boxes.append(b)
        if new_idx == 1:
            self._box2 = b

        trailing_card_col = 6 + self.num_boxes
        trailing_tk_col = trailing_card_col - 1
        pos_trailing = GridPosition(row=2, column=trailing_card_col, region=LayoutRegion.CARD_COMPONENT)
        self.trailing_btn.grid_pos = pos_trailing
        self.trailing_btn.excel_pos = card_to_excel_position(pos_trailing, self.card_slot, self.calc_row)
        self.grid_columnconfigure(trailing_tk_col, minsize=42)
        self.trailing_btn.grid(row=1, column=trailing_tk_col, sticky="nsew", padx=1, pady=1)

        self.card_controls[pos_new] = b
        self.card_controls[pos_trailing] = self.trailing_btn
        self.current_page = self.num_boxes

        try:
            self.update_idletasks()
        except Exception:
            pass

        b.focus_set()

        if self.on_add_box_cb:
            self.on_add_box_cb(self.num_boxes)
        return b

    def _prev_page(self):
        pass

    def _next_page(self):
        pass

    def _flush_active_extra_text(self):
        for i, b in enumerate(self.boxes):
            if hasattr(b, "words_text"):
                self.words_data[i] = b.words_text()
            else:
                self.words_data[i] = b.get()

    def _on_box_change(self, idx, text):
        while len(self.words_data) <= idx:
            self.words_data.append("")
        self.words_data[idx] = text
        if self.on_words_cb:
            self.on_words_cb(idx, text)

    def _on_box_focus(self, idx):
        if self.on_focus_cb:
            self.on_focus_cb(idx)

    def get_words(self):
        self._flush_active_extra_text()
        return tuple(self.words_data[:len(self.boxes)])

    def to_excel_coordinate(self, widget_or_pos):
        p = getattr(widget_or_pos, "grid_pos", widget_or_pos)
        return card_to_excel_position(p, self.card_slot, self.calc_row)

def make_component(parent, center, kind, lead="+", on_pick=None, selected=False,
                   words=None, on_words=None, on_focus=None, card_slot=None, calc_row=1,
                   num_boxes=None, on_add_box=None, as_buttons=False, current_page=None):
    """One card reconstructed on the authoritative 9-column x 3-row Excel grid.

    Columns:
      1: Lead button (Blue + or =)
      2: Empty spacer 1
      3..5: 3x3 directional arrows and center square
      6: Label / Item entry (Box 1)
      7: Context entry (Box 2 / Pager)
      8: Empty spacer 2
      9: Trailing button (Orange +)
    """
    return CardFrame(parent, center, kind, lead=lead, on_pick=on_pick, selected=selected,
                     words=words, on_words=on_words, on_focus=on_focus, card_slot=card_slot,
                     calc_row=calc_row, num_boxes=num_boxes, on_add_box=on_add_box,
                     as_buttons=as_buttons, current_page=current_page)


def _card(parent, item, on_pick=None, selected=False, card_slot=None, calc_row=1, **words):
    kind, text = item
    if kind == "dec":                       # a box the picture draws that is not an input: an ordinary card (a letter, or a square when the picture shows a blank box); only a typed box is blue
        return make_component(parent, text or BOX, "helper", card_slot=card_slot, calc_row=calc_row, **words)
    if kind in ("box", "out"):             # "out" is the formula's answer box: it shows the answer after =, nothing is typed into it
        return make_component(parent, text or BOX, "number", on_pick=on_pick, selected=selected, card_slot=card_slot, calc_row=calc_row, **words)
    return make_component(parent, text, "helper", card_slot=card_slot, calc_row=calc_row, **words)


def _plan(n, levels, fracs, stack_exponents=False):
    """Where every card goes: ({card index: (grid row, column)}, [(row, column, width) of every fraction bar]).  A fraction stacks its numerator on the row above the bar
    and its denominator on the row below, both centred over the bar, which is as wide as the wider of the two; a card inside (an exponent ...) keeps its own level."""
    def parse(indices, depth):
        items, k = [], 0
        while k < len(indices):
            i = indices[k]
            path = fracs[i]
            if len(path) > depth:
                gid = path[depth][0]
                group = []
                while k < len(indices) and len(fracs[indices[k]]) > depth and fracs[indices[k]][depth][0] == gid:
                    group.append(indices[k])
                    k += 1
                num = [j for j in group if fracs[j][depth][1] == "n"]
                den = [j for j in group if fracs[j][depth][1] == "d"]
                items.append(("frac", parse(num, depth + 1), parse(den, depth + 1)))
            else:
                items.append(("card", i))
                k += 1
        return items

    def stacked(items, k):
        """stack_exponents: an exponent card straight after the card it powers shares that card's column (one grid row up) instead of having a column of its own."""
        return stack_exponents and k > 0 and items[k][0] == "card" and items[k - 1][0] == "card" and levels[items[k][1]] == -1

    def width(items):
        return sum(0 if stacked(items, k) else (1 if it[0] == "card" else max(width(it[1]), width(it[2]), 1)) for k, it in enumerate(items))

    placed, bars = {}, []

    def reach(items):
        """(highest, lowest) grid offset of an item list relative to its own line, exponents and nested fractions included."""
        hi = lo = 0
        for it in items:
            if it[0] == "card":
                hi, lo = min(hi, levels[it[1]]), max(lo, levels[it[1]])
            else:
                nb, db = bases(it)
                hi = min(hi, nb + reach(it[1])[0])
                lo = max(lo, db + reach(it[2])[1])
        return hi, lo

    def bases(it):
        """Where a fraction's numerator and denominator lines are, relative to the bar: one row off, or more when an exponent / nested fraction needs the room."""
        return -1 - max(0, reach(it[1])[1]), 1 + max(0, -reach(it[2])[0])

    def place(items, col, base):
        for k, it in enumerate(items):
            if it[0] == "card":
                if stacked(items, k):
                    placed[it[1]] = (base + levels[it[1]], col - 1)
                    continue
                placed[it[1]] = (base + levels[it[1]], col)
                col += 1
            else:
                w = max(width(it[1]), width(it[2]), 1)
                nb, db = bases(it)
                place(it[1], col + (w - width(it[1])) // 2, base + nb)
                place(it[2], col + (w - width(it[2])) // 2, base + db)
                bars.append((base, col, w))
                col += w
        return col

    shown = [i for i in range(n) if not (fracs[i] and fracs[i][-1][1] in ("bar", "hide"))]      # the "/" and the brackets that only wrapped a numerator are not drawn
    end = place(parse(shown, 0), 0, 0)
    return placed, bars, end


def build_row(parent, left, right, stacked=False, on_pick=None, selected=None, levels=None, fracs=None, stack_exponents=False, words=None, on_words=None, on_focus=None, card_slot=None, calc_row=1, num_boxes=None, on_add_box=None):
    """Return a Frame holding the operator row.  left/right are lists of ("box", "") / ("op", text).
    on_pick(index) is called with the position (in `left`) of a box card the user clicks;
    `selected` is the position of the box card to draw as the current target.
    levels = the grid row of every card of `left` (-1 above the line for an exponent, +1 below for a subscript, 0 on the line); every card is its own column.
    fracs = for every card the fractions it is inside (layout.group_fractions): numerators go on the row above the bar and denominators on the row below, always.
    stack_exponents = True puts an exponent card in the column of the card it powers instead of a column of its own (off by default).
    words = for every card of `left` its (label, context); the card's Label and Context boxes then take typed words.  on_words(card index, 0 | 1, text) is called as
    you type; on_focus(card index, 0 | 1) when one of the boxes is clicked."""
    row = tk.Frame(parent, bg=CREAM)
    lv = list(levels or []) + [0] * (len(left) - len(levels or []))
    fr = [list(f) for f in (fracs or [])] + [[] for _ in range(len(left) - len(fracs or []))]
    def word_args(idx):
        """What a card needs so its Label and Context boxes take typed words (nothing: the plain placeholders)."""
        if words is None:
            raw_w = ()
        elif idx < len(words):
            raw_w = tuple(words[idx])
        else:
            raw_w = ()

        if isinstance(num_boxes, dict):
            if idx in num_boxes:
                card_num_boxes = num_boxes[idx]
            else:
                non_empty = sum(1 for w in raw_w if isinstance(w, str) and w.strip())
                card_num_boxes = max(1, non_empty)
        elif num_boxes is not None:
            card_num_boxes = num_boxes
        else:
            non_empty = sum(1 for w in raw_w if isinstance(w, str) and w.strip())
            card_num_boxes = max(1, non_empty)

        return {
            "words": raw_w,
            "num_boxes": card_num_boxes,
            "on_words": (lambda which, text, k=idx: on_words(k, which, text)) if on_words else None,
            "on_focus": (lambda which, k=idx: on_focus(k, which)) if on_focus else None,
            "on_add_box": (lambda count, k=idx: on_add_box(k, count)) if on_add_box else None,
        }

    single_card = (len(left) == 1 and not right and not stacked)
    if stacked:
        cards = [(k, i) for k, i in enumerate(left) if i[0] == "op"]
        col = 0
        for idx, item in cards:
            c_slot = card_slot if idx == 0 else None
            card_frame = _card(row, item, card_slot=c_slot, calc_row=calc_row, **word_args(idx))
            card_frame.card_index = idx
            card_frame.grid(row=1, column=col, padx=(0, 10), pady=0)
            col += 1
        placed, bars = {}, []
    else:
        placed, bars, col = _plan(len(left), lv, fr, stack_exponents)
    top = min([r for r, _c in placed.values()] + [b[0] - 1 for b in bars] + [0])
    for idx, (r, c) in placed.items():
        item = left[idx]
        pick = (lambda k=idx: on_pick(k)) if (on_pick and item[0] == "box") else None
        c_slot = card_slot if idx == 0 else None
        card_frame = _card(row, item, pick, selected == idx, card_slot=c_slot, calc_row=calc_row, **word_args(idx))
        card_frame.card_index = idx          # which card of `left` this is (the cards are created in the order of the grid, not of `left`)
        if single_card:
            card_frame.grid(row=r - top, column=c, sticky="nsew", padx=0, pady=0)
        else:
            card_frame.grid(row=r - top, column=c, padx=(0, 10), pady=0)
    for r, c, w in bars:
        tk.Frame(row, bg="black", height=3).grid(row=r - top, column=c, columnspan=w, sticky="ew", padx=(0, 10))
    if right:
        if placed or stacked:
            tk.Label(row, text="=", bg=CREAM, font=("Segoe UI", 20, "bold")).grid(row=-top, column=col, padx=(0, 10))
            col += 1
        for item in right:
            _card(row, item, card_slot=card_slot, calc_row=calc_row).grid(row=-top, column=col, padx=(0, 10), pady=0)
            col += 1
    return row
