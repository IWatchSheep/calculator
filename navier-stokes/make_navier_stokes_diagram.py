"""Draws navier-stokes/navier_stokes.jpg: the incompressible Navier-Stokes equations, every term in its own column.

    python navier-stokes/make_navier_stokes_diagram.py

The calculator's row rule, applied to one equation (one row):
  every symbol is its own column;
  a derivative is a fraction, numerator above the bar and denominator below;
  an exponent is one line up, in its own column;
  a subscript is one line down, in its own column.
Those lines belong to that one equation. Nothing here is wired into the calculator, and nothing is calculated.
"""
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))


def load_font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts", "segoeuib.ttf" if bold else "seguisym.ttf"),
        os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts", "cambria.ttc"),
    ]
    for path in candidates:
        if os.path.isfile(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


MATH, SMALL = load_font(26), load_font(18)
TITLE, LABEL, NOTE = load_font(28, bold=True), load_font(18), load_font(16)
INK, RULE, GREY = "#1c2b3a", "#dde3ee", "#4a5a78"

# levels inside one equation: -2 exponent of a numerator, -1 numerator, 0 the bar, +1 exponent of a denominator, +2 denominator
# a symbol that is not inside a fraction sits on the bar (level 0); its subscript is one line down (+1)


def numer(text, level=0):
    return (text, -1 if level == 0 else -2)


def denom(text, level=0):
    return (text, 2 if level == 0 else 1)


def first(q, axis):
    """∂q/∂axis, each symbol its own column."""
    return ("frac", [numer("∂"), numer(q)], [denom("∂"), denom(axis)])


def second(q, axis):
    """∂²q/∂axis². The 2 is its own column, one line above the symbol it powers."""
    return ("frac", [numer("∂"), numer("2", -1), numer(q)], [denom("∂"), denom(axis), denom("2", -1)])


def symbol(text, level=0):
    return ("sym", text, level)


def momentum(q, axis):
    """ρ(∂q/∂t + u ∂q/∂x + v ∂q/∂y + w ∂q/∂z) = −∂p/∂axis + μ(∂²q/∂x² + ∂²q/∂y² + ∂²q/∂z²) + f_axis"""
    row = [symbol("ρ"), symbol("("), first(q, "t")]
    for vel, ax in (("u", "x"), ("v", "y"), ("w", "z")):
        row += [symbol("+"), symbol(vel), first(q, ax)]
    row += [symbol(")"), symbol("="), symbol("−"), first("p", axis), symbol("+"), symbol("μ"), symbol("("), second(q, "x")]
    for ax in "yz":
        row += [symbol("+"), second(q, ax)]
    row += [symbol(")"), symbol("+"), symbol("f"), symbol(axis, 1)]
    return row


def continuity():
    row = [first("u", "x")]
    for q, ax in (("v", "y"), ("w", "z")):
        row += [symbol("+"), first(q, ax)]
    row += [symbol("="), symbol("0")]
    return row


def layout(pieces):
    """Columns {level: text} and the inclusive column span of each fraction bar."""
    cols, bars = [], []
    for piece in pieces:
        if piece[0] == "sym":
            cols.append({piece[2]: piece[1]})
            continue
        numer_tokens, denom_tokens = piece[1], piece[2]
        start = len(cols)
        for i in range(max(len(numer_tokens), len(denom_tokens))):
            cell = {}
            if i < len(numer_tokens):
                cell[numer_tokens[i][1]] = numer_tokens[i][0]
            if i < len(denom_tokens):
                cell[denom_tokens[i][1]] = denom_tokens[i][0]
            cols.append(cell)
        bars.append((start, len(cols) - 1))
    return cols, bars


def draw_equation(d, cols, bars, left, bar_y):
    probe = d
    gap = 7

    def tw(text, font=MATH):
        return probe.textlength(text, font=font) if text else 0

    widths = []
    for cell in cols:
        widest = 16
        for level, text in cell.items():
            font = SMALL if level in (-2, 1) else MATH
            widest = max(widest, tw(text, font) + 4)
        widths.append(widest)
    xs, x = [], left
    for w in widths:
        xs.append(x)
        x += w + gap
    right = x

    def y_of(level):
        return bar_y + { -2: -62, -1: -34, 0: 0, 1: 30, 2: 58 }[level]

    for start, end in bars:
        x0 = xs[start]
        x1 = xs[end] + widths[end]
        probe.line((x0, bar_y, x1, bar_y), fill=INK, width=3)
    for i, cell in enumerate(cols):
        for level, text in cell.items():
            font = SMALL if level in (-2, 1) else MATH
            cx = xs[i] + widths[i] / 2
            probe.text((cx, y_of(level)), text, font=font, fill=INK, anchor="mm")
    return right


def main():
    equations = [
        ("x, the velocity component u", momentum("u", "x")),
        ("y, the velocity component v", momentum("v", "y")),
        ("z, the velocity component w", momentum("w", "z")),
        ("Continuity. The fluid is incompressible, so the volume does not change.", continuity()),
    ]
    laid = [(title, *layout(pieces)) for title, pieces in equations]
    width = 80 + max(sum(1 for _ in cols) for _title, cols, _bars in ((t, c, b) for t, c, b in laid)) * 4
    # measure real width with a throwaway image
    scratch = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    # draw_equation needs the real draw for textlength; build image after measuring via a first pass on a wide canvas
    measure = Image.new("RGB", (4000, 200), "white")
    md = ImageDraw.Draw(measure)
    extents = []
    for title, cols, bars in laid:
        extents.append(draw_equation(md, cols, bars, 48, 80))
    width = int(max(extents) + 56)
    band = 168
    head = 118
    height = head + band * len(laid) + 70
    img = Image.new("RGB", (width, height), "white")
    d = ImageDraw.Draw(img)
    d.text((40, 28), "Navier–Stokes equations, every term in its own column", font=TITLE, fill="#16233a")
    d.text((40, 68), "Incompressible Newtonian fluid, constant viscosity. One equation is one row: the lines above and below a bar belong to that row.", font=LABEL, fill=GREY)
    d.line((36, 98, width - 36, 98), fill=RULE, width=3)
    y = head + 78
    for (title, cols, bars), _extent in zip(laid, extents):
        d.text((40, y - 78), title, font=LABEL, fill=GREY)
        draw_equation(d, cols, bars, 48, y)
        y += band
        d.line((36, y - 86, width - 36, y - 86), fill=RULE, width=2)
    d.text((40, height - 36),
           "ρ density    μ dynamic viscosity    p pressure    f force per volume    u, v, w velocity along x, y, z    t time",
           font=NOTE, fill=GREY)
    path = os.path.join(HERE, "navier_stokes.jpg")
    img.save(path, "JPEG", quality=92)
    print("wrote", path, img.size)


if __name__ == "__main__":
    main()
