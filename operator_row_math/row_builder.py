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


def build_row(parent, left, right, stacked=False, on_pick=None, selected=None, levels=None, fracs=None, stack_exponents=False):
    """Return a Frame holding the operator row.  left/right are lists of ("box", "") / ("op", text).
    on_pick(index) is called with the position (in `left`) of a box card the user clicks;
    `selected` is the position of the box card to draw as the current target.
    levels = the grid row of every card of `left` (-1 above the line for an exponent, +1 below for a subscript, 0 on the line); every card is its own column.
    fracs = for every card the fractions it is inside (layout.group_fractions): numerators go on the row above the bar and denominators on the row below, always.
    stack_exponents = True puts an exponent card in the column of the card it powers instead of a column of its own (off by default)."""
    row = tk.Frame(parent, bg=CREAM)
    lv = list(levels or []) + [0] * (len(left) - len(levels or []))
    fr = [list(f) for f in (fracs or [])] + [[] for _ in range(len(left) - len(fracs or []))]
    if stacked:
        cards = [(None, i) for i in left if i[0] == "op"]
        col = 0
        for idx, item in cards:
            _card(row, item).grid(row=1, column=col, padx=(0, 10), pady=4)
            col += 1
        placed, bars = {}, []
    else:
        placed, bars, col = _plan(len(left), lv, fr, stack_exponents)
    top = min([r for r, _c in placed.values()] + [b[0] - 1 for b in bars] + [0])
    for idx, (r, c) in placed.items():
        item = left[idx]
        pick = (lambda k=idx: on_pick(k)) if (on_pick and item[0] == "box") else None
        _card(row, item, pick, selected == idx).grid(row=r - top, column=c, padx=(0, 10), pady=4)
    for r, c, w in bars:
        tk.Frame(row, bg="black", height=3).grid(row=r - top, column=c, columnspan=w, sticky="ew", padx=(0, 10))
    if right:
        if placed or stacked:
            tk.Label(row, text="=", bg=CREAM, font=("Segoe UI", 20, "bold")).grid(row=-top, column=col, padx=(0, 10))
            col += 1
        for item in right:
            _card(row, item).grid(row=-top, column=col, padx=(0, 10), pady=4)
            col += 1
    return row
