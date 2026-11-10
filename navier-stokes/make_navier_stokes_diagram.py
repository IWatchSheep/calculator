"""Draws the Navier-Stokes pictures.

    python navier-stokes/make_navier_stokes_diagram.py

navier-stokes/navier_stokes.jpg   the whole set of equations (incompressible Newtonian fluid): vector form, the x, y, z momentum lines, continuity.
and one picture for each operator of the project (operators_one_operator_per_file/physics/physics/<operator>/<operator>.jpg):
    navier_stokes_equation (the whole set), navier_stokes_x_momentum, navier_stokes_y_momentum, navier_stokes_z_momentum, navier_stokes_continuity.

Written the way the rows write math: every derivative is a fraction with its numerator on the line above the bar and its denominator on the line below,
and an exponent sits one line up, over the symbol it powers.
"""
import os
import shutil

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OPS = os.path.join(ROOT, "operators_one_operator_per_file", "physics", "physics")
FONTS = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts")


def font(name, size, index=0):
    return ImageFont.truetype(os.path.join(FONTS, name), size, index=index)


MATH, SMALL = font("cambria.ttc", 38, 1), font("cambria.ttc", 25, 1)      # Cambria Math has the \u2202 \u2207 symbols
LABEL, TITLE, NOTE = font("cambria.ttc", 24, 1), font("segoeuib.ttf", 30), font("cambria.ttc", 19, 1)
INK, RULE, GREY = "#1c2b3a", "#dde3ee", "#4a5a78"
img = d = None


def new(w, h):
    global img, d
    img = Image.new("RGB", (int(w), int(h)), "white")
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
    return put(put(x, base, s), base + 8, low, SMALL)


def op(x, base, s):
    return put(x + 8, base, s) + 8


def vector(x, base):
    x = put(x, base, "\u03c1 (") + 4
    x = frac(x, base, "\u2202u", "\u2202t")
    x = op(x, base, "+")
    x = put(x, base, "(u \u00b7 \u2207) u") + 4
    x = put(x, base, ")") + 6
    x = op(x, base, "=")
    x = put(x, base, "\u2212\u2207p") + 6
    x = op(x, base, "+")
    x = put(x, base, "\u03bc \u2207")
    put(x, base - 24, "2", SMALL)
    x = put(x + 16, base, "u") + 6
    x = op(x, base, "+")
    return put(x, base, "f")


def component(x, base, q, axis):
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
    return sub(x, base, "f", axis)


def continuity(x, base):
    x = frac(x, base, "\u2202u", "\u2202x")
    x = op(x, base, "+")
    x = frac(x, base, "\u2202v", "\u2202y")
    x = op(x, base, "+")
    x = frac(x, base, "\u2202w", "\u2202z")
    return put(op(x, base, "="), base, "0")


def whole_set():
    new(1320, 970)
    d.text((44, 22), "Navier\u2013Stokes equations (incompressible Newtonian fluid)", font=TITLE, fill="#16233a")
    d.line((40, 70, 1280, 70), fill=RULE, width=3)
    put(44, 128, "Vector form", LABEL, GREY)
    vector(44, 205)
    d.line((40, 270, 1280, 270), fill=RULE, width=2)
    put(44, 312, "Written out, one line for each direction (u, v, w are the velocity components along x, y, z)", LABEL, GREY)
    base = 395
    for q, axis in (("u", "x"), ("v", "y"), ("w", "z")):
        component(44, base, q, axis)
        base += 118
    d.line((40, base - 62, 1280, base - 62), fill=RULE, width=2)
    put(44, base - 28, "Continuity (the fluid is incompressible)", LABEL, GREY)
    continuity(44, base + 52)
    d.text((44, 970 - 42), "\u03c1 density     \u03bc dynamic viscosity     p pressure     f force per volume (gravity ...)     t time     x, y, z position     "
           "\u2207 gradient     \u2207\u00b2 Laplacian", font=NOTE, fill=GREY)
    return img


def single(title, draw, description, base=185):
    """One equation, in the look of the other operator pictures: title, rule, the equation, a description line."""
    new(10, 10)
    end = draw(0, base)
    w = max(1040, int(end) + 88)
    new(w, base + 130)
    d.text((40, 18), title, font=font("segoeuib.ttf", 30), fill="#16233a")
    d.line((36, 67, w - 36, 67), fill=RULE, width=3)
    draw((w - end) / 2, base)
    d.text((40, base + 92), description, font=NOTE, fill=GREY)
    return img


def save(image, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    image.save(path, "JPEG", quality=92)
    print("wrote", path)


if __name__ == "__main__":
    whole = whole_set()
    save(whole, os.path.join(HERE, "navier_stokes.jpg"))
    shutil.copyfile(os.path.join(HERE, "navier_stokes.jpg"), os.path.join(OPS, "navier_stokes_equation", "navier_stokes_equation.jpg"))
    for q, axis in (("u", "x"), ("v", "y"), ("w", "z")):
        pic = single("Navier\u2013Stokes: %s momentum" % axis, lambda x, b, q=q, a=axis: component(x, b, q, a),
                     "Momentum balance along %s for an incompressible fluid. %s is the velocity along %s; \u03c1 density, \u03bc viscosity, p pressure, f_%s force per volume." % (axis, q, axis, axis))
        save(pic, os.path.join(OPS, "navier_stokes_%s_momentum" % axis, "navier_stokes_%s_momentum.jpg" % axis))
    save(single("Navier\u2013Stokes: continuity (incompressible)", continuity,
                "The fluid is incompressible, so the velocity field has no sources or sinks: u, v, w are the velocity along x, y, z."),
         os.path.join(OPS, "navier_stokes_continuity", "navier_stokes_continuity.jpg"))
