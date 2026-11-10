"""Draws navier-stokes/navier_stokes.jpg: the incompressible Navier-Stokes equations, written the way the rows write math
(a fraction has its numerator above the bar and its denominator below; an exponent is one line up).

    python navier-stokes/make_navier_stokes_diagram.py

Same look as operators_one_operator_per_file/*/*.jpg (title, rule, formula, description line).  The blue boxes are the symbols a row would take as inputs.
"""
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts")


def font(name, size, index=0):
    return ImageFont.truetype(os.path.join(FONTS, name), size, index=index)


MATH, SMALL = font("cambria.ttc", 46, 1), font("cambria.ttc", 29, 1)
TITLE, TEXT, NOTE = font("segoeuib.ttf", 30), font("segoeui.ttf", 19), font("segoeui.ttf", 17)
INK, BLUE_FILL, BLUE_LINE, RULE = "#1c2b3a", "#e3edf8", "#3d6a9e", "#dde3ee"
W, H = 1180, 700
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
d.text((40, 24), "Navier\u2013Stokes equations (incompressible flow)", font=TITLE, fill="#16233a")
d.line((36, 68, W - 36, 68), fill=RULE, width=3)


def width(s, f=MATH):
    return d.textlength(s, font=f)


def put(x, base, s, f=MATH, fill=INK):
    d.text((x, base), s, font=f, fill=fill, anchor="ls")
    return x + width(s, f)


def boxed(x, base, s, f=MATH, sub=None):
    """A blue input box holding a symbol (and its subscript)."""
    w = width(s, f) + (width(sub, SMALL) if sub else 0) + 18
    d.rectangle((x, base - 44, x + w, base + 14), fill=BLUE_FILL, outline=BLUE_LINE, width=2)
    put(x + 9, base, s, f)
    if sub:
        put(x + 9 + width(s, f), base + 8, sub, SMALL)
    return x + w + 8


def frac(x, base, top, bottom, f=MATH):
    """numerator on the line above the bar, denominator on the line below"""
    w = max(width(top, f), width(bottom, f)) + 14
    d.line((x, base - 17, x + w, base - 17), fill=INK, width=3)
    d.text((x + w / 2, base - 26), top, font=f, fill=INK, anchor="ms")
    d.text((x + w / 2, base + 42), bottom, font=f, fill=INK, anchor="ms")
    return x + w + 6


def momentum(x, base):
    """The momentum equation starting at x on the line `base`; returns where it ends."""
    x = boxed(x, base, "\u03c1")
    x = put(x, base, "(") + 4
    x = frac(x, base, "\u2202u", "\u2202t") + 4
    x = put(x, base, "+") + 10
    x = put(x, base, "(u \u00b7 \u2207)u") + 2
    x = put(x, base, ")") + 18
    x = put(x, base, "=") + 18
    x = put(x, base, "\u2212\u2207p") + 14
    x = put(x, base, "+") + 12
    x = boxed(x, base, "\u03bc")
    x = put(x, base, "\u2207") + 0
    put(x, base - 26, "2", SMALL)
    x = put(x + 16, base, "u") + 14
    x = put(x, base, "+") + 12
    x = boxed(x, base, "f")
    return x


momentum(44, 205)

# ---- continuity equation
base2 = 330
x = put(44, base2, "\u2207 \u00b7 u  =  0") + 40
put(x, base2 - 4, "(incompressible: the density \u03c1 is constant)", NOTE, "#4a5a78")

# ---- what each term is
d.line((36, 395, W - 36, 395), fill=RULE, width=2)
terms = [
    ("\u03c1 \u2202u/\u2202t", "inertia: how the momentum of the fluid changes in time"),
    ("\u03c1 (u \u00b7 \u2207)u", "convection: momentum carried along by the flow itself"),
    ("\u2212\u2207p", "pressure gradient: fluid is pushed from high to low pressure"),
    ("\u03bc \u2207\u00b2u", "viscosity: friction between neighbouring layers of fluid"),
    ("f", "body force per volume: gravity, or any other outside force"),
]
y = 420
for sym, text in terms:
    put(60, y + 8, sym, font("cambria.ttc", 25, 1))
    put(290, y + 6, text, TEXT, "#34455f")
    y += 38
LEGEND = font("cambria.ttc", 19, 1)       # Cambria Math has the ∂ ∇ symbols; Segoe UI does not
d.text((40, H - 70), "u = velocity field     p = pressure     ρ = density     μ = dynamic viscosity     f = body force per volume", font=LEGEND, fill="#4a5a78")
d.text((40, H - 40), "∂/∂t = rate of change in time     ∇ = gradient     ∇² = Laplacian (sum of the second derivatives in x, y, z)", font=LEGEND, fill="#4a5a78")
img.save(os.path.join(HERE, "navier_stokes.jpg"), "JPEG", quality=92)
print("wrote", os.path.join(HERE, "navier_stokes.jpg"))

# ---- the picture for operators_one_operator_per_file/physics/physics/navier_stokes_equation/ (same look as the other operator pictures)
ROOT = os.path.dirname(HERE)
d = ImageDraw.Draw(Image.new("RGB", (10, 10)))          # measure first
end = momentum(0, 0)
img = Image.new("RGB", (1040, 300), "white")
d = ImageDraw.Draw(img)
d.text((40, 30), "Navier–Stokes equation", font=font("segoeuib.ttf", 30), fill="#16233a")
d.line((36, 67, 1004, 67), fill="#dde1ee", width=3)
momentum((1040 - end) / 2, 175)
d.text((40, 262), "Momentum of an incompressible fluid. ρ is the density, μ the viscosity, f the force on each volume; ∇·u = 0.", font=font("cambria.ttc", 19, 1), fill="#4a5a78")
out = os.path.join(ROOT, "operators_one_operator_per_file", "physics", "physics", "navier_stokes_equation", "navier_stokes_equation.jpg")
os.makedirs(os.path.dirname(out), exist_ok=True)
img.save(out, "JPEG", quality=92)
print("wrote", out)
