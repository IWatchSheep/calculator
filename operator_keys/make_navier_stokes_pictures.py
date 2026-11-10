"""Draws the pictures of the five Navier-Stokes operators (incompressible Newtonian fluid), FROM THEIR ROWS.

    python operator_keys/make_navier_stokes_pictures.py

One picture for each operator, written to operators_one_operator_per_file/physics/physics/<operator>/<operator>.jpg:
    navier_stokes_equation, navier_stokes_x_momentum, navier_stokes_y_momentum, navier_stokes_z_momentum, navier_stokes_continuity.

The picture is drawn from the cards of the operator's row (operator_row_math/physics/physics/<operator>/<operator>.py: LEFT, LEVELS, FRAC, STACK_EXPONENTS), placed by the
same planner the calculator uses (row_builder._plan).  Every card is ONE glyph in its own column and grid row; nothing is drawn as a longer string: a derivative is a
numerator card or two above its bar and a denominator card or two below it, an exponent is a small card one grid row up in the column of the symbol it powers.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
import operator_row_math as R  # noqa: E402
from operator_row_math.row_builder import _plan  # noqa: E402

OPS = os.path.join(ROOT, "operators_one_operator_per_file", "physics", "physics")
FONTS = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts")
PREFIX = "physics/physics/"


def font(name, size, index=0):
    try:
        return ImageFont.truetype(os.path.join(FONTS, name), size, index=index)
    except OSError:
        fallback = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if "bold" in name or name.endswith("b.ttf") else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        return ImageFont.truetype(fallback, size)


BIG, SMALL = font("cambria.ttc", 38, 1), font("cambria.ttc", 25, 1)      # Cambria Math has the ∂ ∇ symbols
NOTE = font("cambria.ttc", 19, 1)
INK, RULE, GREY = "#1c2b3a", "#dde3ee", "#4a5a78"
PAD, ROW_BIG, ROW_SMALL = 16, 56, 34          # space added to a column, height of a grid row with ordinary cards, height of one that holds only exponents / subscripts
_probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))


BOX = "□"
BOX_W, BOX_H = 46, 46


def cards_of(key):
    """The placed cards of an operator's row: ({card index: (text, small, grid row, column, is_box)}, bars, columns, words).  A box card (an input, the answer, or a blank
    box the picture draws) is_box: it is drawn as a blue box, with its text (if any) inside."""
    m = R.get(key if "/" in key else PREFIX + key)
    levels = list(getattr(m, "LEVELS", None) or [0] * len(m.LEFT))
    fracs = list(getattr(m, "FRAC", None) or [[] for _ in m.LEFT])
    placed, bars, columns = _plan(len(m.LEFT), levels, fracs, bool(getattr(m, "STACK_EXPONENTS", False)))
    cards = {i: (m.LEFT[i][1], levels[i] != 0, r, c, m.LEFT[i][0] != "op") for i, (r, c) in placed.items()}
    return cards, bars, columns, getattr(m, "WORDS", {})


def layout(key):
    cards, bars, columns, words = cards_of(key)
    colw = [34] * columns
    for text, small, r, c, is_box in cards.values():
        w = max(BOX_W, _probe.textlength(text, font=BIG) + 22) if is_box else _probe.textlength(text, font=SMALL if small else BIG) + PAD
        colw[c] = max(colw[c], w)
    for r, c, w in bars:
        for cc in range(c, c + w):
            colw[cc] = max(colw[cc], 34)
    grid_rows = sorted({r for _t, _s, r, _c, _b in cards.values()} | {b[0] for b in bars})
    first = grid_rows[0]
    heights = {}
    for g in range(first, grid_rows[-1] + 1):
        big = any(r == g and not small for _t, small, r, _c, _b in cards.values()) or any(b[0] == g for b in bars)
        heights[g] = ROW_BIG if big else ROW_SMALL
    return cards, bars, colw, heights, first, words


WORD = font("segoeui.ttf", 15)
SYMBOL = font("cambria.ttc", 19, 1)          # Cambria Math has the ∂ ∇ symbols Segoe UI lacks
BLUE_FILL, BLUE_LINE = "#d6e6fb", "#2a6ec9"


def draw_box(d, cx, cy, text=""):
    """A blue box centred at (cx, cy), the symbol (if the card has one) inside it."""
    w = max(BOX_W, _probe.textlength(text, font=BIG) + 22)
    d.rounded_rectangle((cx - w / 2, cy - BOX_H / 2, cx + w / 2, cy + BOX_H / 2), radius=6, fill=BLUE_FILL, outline=BLUE_LINE, width=3)
    if text:
        d.text((cx, cy + 0.30 * 38), text, font=BIG, fill="#1b3f7a", anchor="ms")


def word_lines(cards, words):
    """One line for every different card that has words: (card, label, context).  The same words on the same symbol twice (dim A + dim B) are listed once."""
    out, seen = [], set()
    for i in sorted(words):
        if i not in cards:
            continue
        label, context = words[i]
        symbol = cards[i][0] if not cards[i][4] else ""
        if (symbol, label, context) in seen:
            continue
        seen.add((symbol, label, context))
        out.append((cards[i], label, context))
    return out


def render(key, title, description):
    cards, bars, colw, heights, first, words = layout(key)
    formula_w, formula_h = sum(colw), sum(heights.values())
    lines = description.split("\n") if description else []
    word_rows = word_lines(cards, words)
    w = max(1040, int(formula_w) + 88)
    top = 100                                              # the equation starts under the title and its rule
    words_y = top + formula_h + 16
    desc_y = words_y + 24 * len(word_rows) + (16 if word_rows else 0)
    img = Image.new("RGB", (w, desc_y + 26 * len(lines) + 24), "white")
    d = ImageDraw.Draw(img)
    d.text((40, 18), title, font=font("segoeuib.ttf", 30), fill="#16233a")
    d.line((36, 67, w - 36, 67), fill=RULE, width=3)
    xs, x = [], (w - formula_w) / 2
    for cw in colw:
        xs.append(x)
        x += cw
    ys, y = {}, top
    for g in range(first, first + len(heights)):
        ys[g] = y + heights[g] / 2
        y += heights[g]
    for text, small, r, c, is_box in cards.values():
        cx, cy = xs[c] + colw[c] / 2, ys[r]
        if is_box:
            draw_box(d, cx, cy, text)
        elif small:
            d.text((cx, cy + 0.30 * 25), text, font=SMALL, fill=INK, anchor="ms")
        else:
            d.text((cx, cy + 0.30 * 38), text, font=BIG, fill=INK, anchor="ms")
    for r, c, bw in bars:
        d.line((xs[c] + 3, ys[r], xs[c + bw - 1] + colw[c + bw - 1] - 3, ys[r]), fill=INK, width=3)
    # the words: one line for each card that has them, its symbol (a box exactly as drawn above) then its label and context
    for n, ((text, small, r, c, is_box), label, context) in enumerate(word_rows):
        ly = words_y + 24 * n + 10
        if is_box:
            small_box = Image.new("RGB", (88, 64), "white")
            draw_box(ImageDraw.Draw(small_box), 44, 32, text)
            small_box = small_box.resize((int(88 * 0.5), int(64 * 0.5)), Image.LANCZOS)
            img.paste(small_box, (40, ly - small_box.height // 2))
        else:
            d.text((40, ly), text, font=SYMBOL, fill=INK, anchor="lm")
        d.text((128, ly), "%s  -  %s" % (label, context), font=WORD, fill=GREY, anchor="lm")
    for k, line in enumerate(lines):
        d.text((40, desc_y + 26 * k), line, font=NOTE, fill=GREY)
    return img


def save(image, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    image.save(path, "JPEG", quality=92)
    print("wrote", path)


PICTURES = [
    ("navier_stokes_equation", "Navier\u2013Stokes equation",
     "Density times the fluid's acceleration equals the push of pressure, the friction of the fluid on itself and any outside force.\n"
     "u velocity, \u03c1 density, \u03bc viscosity, p pressure, f force per volume (such as gravity)."),
]
for _q, _axis in (("u", "x"), ("v", "y"), ("w", "z")):
    PICTURES.append(("navier_stokes_%s_momentum" % _axis, "Navier\u2013Stokes: %s momentum" % _axis,
                     "Momentum balance along %s for an incompressible fluid. %s is the velocity along %s; \u03c1 density, \u03bc viscosity, p pressure, f_%s force per volume."
                     % (_axis, _q, _axis, _axis)))
PICTURES.append(("navier_stokes_continuity", "Navier\u2013Stokes: continuity (incompressible)",
                 "The fluid is incompressible, so the velocity field has no sources or sinks: u, v, w are the velocity along x, y, z."))

if __name__ == "__main__":
    extra = [a for a in sys.argv[1:] if not a.startswith("--")]
    if extra:
        for key in extra:
            name = key.split("/")[-1]
            title = R.get(key).NAME
            import operators_one_operator_per_file as library
            save(render(key, title, library.get(key).FORMULA), os.path.join(ROOT, "operators_one_operator_per_file", *key.split("/"), name + ".jpg"))
    else:
        for slug, title, description in PICTURES:
            save(render(slug, title, description), os.path.join(OPS, slug, slug + ".jpg"))
