"""Solve for x   [solve]

Category : Math > Algebra
Formula  : Find the value(s) of x that make an equation true

Status   : ready to use - call compute(f)
"""

NAME = 'Solve for x'
SYMBOL = 'solve'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = 'Find the value(s) of x that make an equation true'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f):
    """Real x with f(x) = 0 between −100 and 100  (type the equation as left − right, e.g. x**2 - 4)"""
    n, lo, hi = 40000, -100.0, 100.0
    roots, prev = [], None
    for i in range(n + 1):
        x = lo + (hi - lo) * i / n
        try:
            y = f(x)
        except (ZeroDivisionError, ValueError, OverflowError):
            prev = None
            continue
        if abs(y) < 1e-12:
            roots.append(x)
        elif prev is not None and prev[1] * y < 0:
            a, b = prev[0], x
            for _ in range(80):
                m = (a + b) / 2
                if f(a) * f(m) <= 0:
                    b = m
                else:
                    a = m
            roots.append((a + b) / 2)
        prev = (x, y)
    out = []
    for r in roots:
        r = round(r, 9)
        if not out or abs(r - out[-1]) > 1e-6:
            out.append(r)
    return out
