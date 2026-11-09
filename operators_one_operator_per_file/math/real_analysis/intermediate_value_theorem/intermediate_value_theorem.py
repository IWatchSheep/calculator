"""Intermediate value theorem   [IVT]

Category : Math > Real analysis
Formula  : If f is continuous on [a, b] then f takes every value between f(a) and f(b)

Status   : ready to use - call compute(f, a, b, y)
"""

NAME = 'Intermediate value theorem'
SYMBOL = 'IVT'
CATEGORY = 'Math'
SUBCATEGORY = 'Real analysis'
FORMULA = 'If f is continuous on [a, b] then f takes every value between f(a) and f(b)'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, a, b, y):
    """A point c in [a, b] with f(c) = y  (f continuous, y between f(a) and f(b))"""
    fa, fb = f(a) - y, f(b) - y
    if fa * fb > 0:
        raise ValueError("y is not between f(a) and f(b)")
    for _ in range(100):
        m = (a + b) / 2
        if (f(a) - y) * (f(m) - y) <= 0:
            b = m
        else:
            a = m
    return (a + b) / 2
