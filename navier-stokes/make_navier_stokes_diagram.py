"""Draws navier-stokes/navier_stokes.jpg: the Navier-Stokes equations for an incompressible Newtonian fluid, written out in full.

    python navier-stokes/make_navier_stokes_diagram.py

Shown: the vector form, then the same momentum equation as three lines (the x, y and z components, with u, v, w the velocity components), then the
continuity equation.  Written the way the rows write math: every derivative is a fraction with its numerator on the line above the bar and its denominator
on the line below, and an exponent sits one line up.  Nothing here is wired into the calculator.
"""
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts")


def font(name, size, index=0):
    return ImageFont.truetype(os.path.join(FONTS, name), size, index=index)


MATH, SMALL = font("cambria.ttc", 38, 1), font("cambria.ttc", 25, 1)      # Cambria Math has the \u2202 \u2207 symbols
LABEL, TITLE, NOTE = font("cambria.ttc", 24, 1), font("segoeuib.ttf", 30), font("cambria.ttc", 19, 1)
INK, RULE, GREY = "#1c2b3a", "#dde3ee", "#4a5a78"
W, H = 1320, 970
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def width(s, f=MATH):
    return d.textlength(s, font=f)


def put(x, base, s, f=MATH, fill=INK):
    d.text((x, base), s, font=f, fill=fill, anchor="ls")
    return x + width(s, f)


def frac(x, base, top, bottom):
    """a derivative: numerator on the line above the bar, denominator on the line below"""
    w = max(width(top), width(bottom)) + 12
    d.line((x, base - 14, x + w, base - 14), fill=INK, width=3)
    d.text((x + w / 2, base - 24), top, font=MATH, fill=INK, anchor="ms")
    d.text((x + w / 2, base + 38), bottom, font=MATH, fill=INK, anchor="ms")
    return x + w + 6


def sub(x, base, s, low):
    x = put(x, base, s)
    return put(x, base + 8, low, SMALL)


def op(x, base, s):
    return put(x + 8, base, s) + 8


def component(x, base, q, axis, f_name):
    """rho ( dq/dt + u dq/dx + v dq/dy + w dq/dz ) = - dp/d(axis) + mu ( d2q/dx2 + d2q/dy2 + d2q/dz2 ) + f_axis"""
    x = put(x, base, "\u03c1 (") + 4
    x = frac(x, base, "\u2202" + q, "\u2202t")
    for vel, ax in (("u", "x"), ("v", "y"), ("w", "z")):
        x = op(x, base, "+")
        x = put(x, base, vel) + 2
        x = frac(x, base, "\u2202" + q, "\u2202" + ax)
    x = put(x, base, ")") + 6
    x = op(x, base, "=")
    x = put(x, base, "\u2212") + 4
    x = frac(x, base, "\u2202p", "\u2202" + axis)
    x = op(x, base, "+")
    x = put(x, base, "\u03bc (") + 4
    for k, ax in enumerate("xyz"):
        if k:
            x = op(x, base, "+")
        x = frac(x, base, "\u2202\u00b2" + q, "\u2202" + ax + "\u00b2")
    x = put(x, base, ")") + 6
    x = op(x, base, "+")
    return sub(x, base, "f", f_name)


d.text((44, 22), "Navier\u2013Stokes equations (incompressible Newtonian fluid)", font=TITLE, fill="#16233a")
d.line((40, 70, W - 40, 70), fill=RULE, width=3)

# ---- vector form
put(44, 128, "Vector form", LABEL, GREY)
x = put(44, 205, "\u03c1 (") + 4
x = frac(x, 205, "\u2202u", "\u2202t")
x = op(x, 205, "+")
x = put(x, 205, "(u \u00b7 \u2207) u") + 4
x = put(x, 205, ")") + 6
x = op(x, 205, "=")
x = put(x, 205, "\u2212\u2207p") + 6
x = op(x, 205, "+")
x = put(x, 205, "\u03bc \u2207") + 0
put(x, 205 - 24, "2", SMALL)
x = put(x + 16, 205, "u") + 6
x = op(x, 205, "+")
put(x, 205, "f")

# ---- the three components
d.line((40, 270, W - 40, 270), fill=RULE, width=2)
put(44, 312, "Written out, one line for each direction (u, v, w are the velocity components along x, y, z)", LABEL, GREY)
base = 395
for q, axis, name in (("u", "x", "x"), ("v", "y", "y"), ("w", "z", "z")):
    component(44, base, q, axis, name)
    base += 118

# ---- continuity
d.line((40, base - 62, W - 40, base - 62), fill=RULE, width=2)
put(44, base - 28, "Continuity (the fluid is incompressible)", LABEL, GREY)
x = frac(44, base + 52, "\u2202u", "\u2202x")
x = op(x, base + 52, "+")
x = frac(x, base + 52, "\u2202v", "\u2202y")
x = op(x, base + 52, "+")
x = frac(x, base + 52, "\u2202w", "\u2202z")
put(op(x, base + 52, "="), base + 52, "0")

d.text((44, H - 42), "\u03c1 density     \u03bc dynamic viscosity     p pressure     f force per volume (gravity ...)     t time     x, y, z position     "
       "\u2207 gradient     \u2207\u00b2 Laplacian", font=NOTE, fill=GREY)
img.save(os.path.join(HERE, "navier_stokes.jpg"), "JPEG", quality=92)
print("wrote", os.path.join(HERE, "navier_stokes.jpg"))
