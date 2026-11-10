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
from gui_style import ARROWS, ARROW_BG, BLUE, CREAM, PALE_BLUE, PALE_ORANGE, btn  # noqa: E402

BOX = "□"


def make_component(parent, center, kind, lead="+", on_pick=None, selected=False):
    """One card.  kind: 'number' (blue centre) or 'helper' (yellow centre = operator card).
    lead: text of the first button (blue "+"; the result card of a row uses "=").
    on_pick: called when the blue + or the centre box is clicked (selects this card to be expanded).
    selected: draw the centre box as the current target."""
    pick = on_pick or (lambda: None)
    f = tk.Frame(parent, bg=CREAM)
    btn(f, lead, PALE_BLUE, fg=BLUE if lead == "+" else "black", font=("Segoe UI", 14, "bold"), width=3,
        highlightbackground=BLUE, command=pick).grid(row=0, column=0, rowspan=3, padx=(0, 10))
    grid = tk.Frame(f, bg=CREAM)
    grid.grid(row=0, column=1, rowspan=3)
    for r in range(3):
        for c in range(3):
            sym = ARROWS[r][c]
            if sym:
                tk.Button(grid, text=sym, width=2, bg=ARROW_BG, relief="groove",
                          command=lambda: None).grid(row=r, column=c, padx=1, pady=1)
            else:
                bg = "#fbd34d" if kind == "helper" else PALE_BLUE
                if selected:
                    bg = "#5b9bf0"
                f.center_btn = tk.Button(grid, text=center, width=max(2, len(center) + 1), bg=bg,
                                         relief="sunken" if selected else "solid", bd=3 if selected else 1,
                                         font=("Segoe UI", 12, "bold"), command=pick)
                f.center_btn.grid(row=r, column=c, padx=1, pady=1)
    label = "[Label]" if kind == "helper" else "[Item]"
    tk.Button(f, text=label, font=("Segoe UI", 12), bg="white", relief="solid", bd=1,
              width=7, command=lambda: None).grid(row=0, column=2, rowspan=3, padx=6, ipady=4)
    tk.Button(f, text="[Context]", font=("Segoe UI", 12), bg="white", relief="solid", bd=1,
              width=9, command=lambda: None).grid(row=0, column=3, rowspan=3, padx=(0, 6), ipady=4)
    btn(f, "+", PALE_ORANGE, fg="#c07000", font=("Segoe UI", 14, "bold"), width=3,
        highlightbackground="#e0a060").grid(row=0, column=4, rowspan=3, padx=(0, 4))
    return f


def _card(parent, item, on_pick=None, selected=False):
    kind, text = item
    if kind == "dec":                       # a box the picture draws that is not an input: an ordinary card (a letter, or a square when the picture shows a blank box); only a typed box is blue
        return make_component(parent, text or BOX, "helper")
    if kind in ("box", "out"):             # "out" is the formula's answer box: it shows the answer after =, nothing is typed into it
        return make_component(parent, text or BOX, "number", on_pick=on_pick, selected=selected)
    return make_component(parent, text, "helper")


def build_row(parent, left, right, stacked=False, on_pick=None, selected=None):
    """Return a Frame holding the operator row.  left/right are lists of ("box", "") / ("op", text).
    on_pick(index) is called with the position (in `left`) of a box card the user clicks;
    `selected` is the position of the box card to draw as the current target."""
    row = tk.Frame(parent, bg=CREAM)
    if stacked:
        cards = [(None, i) for i in left if i[0] == "op"]
    else:
        cards = list(enumerate(left))
    col = 0
    for idx, item in cards:
        pick = (lambda k=idx: on_pick(k)) if (on_pick and idx is not None and item[0] == "box") else None
        _card(row, item, pick, selected == idx and idx is not None).grid(row=0, column=col, padx=(0, 10), pady=4)
        col += 1
    if right:
        if cards:
            tk.Label(row, text="=", bg=CREAM, font=("Segoe UI", 20, "bold")).grid(row=0, column=col, padx=(0, 10))
            col += 1
        for item in right:
            _card(row, item).grid(row=0, column=col, padx=(0, 10), pady=4)
            col += 1
    return row
