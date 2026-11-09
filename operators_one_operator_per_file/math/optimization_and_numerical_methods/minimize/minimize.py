"""Minimize   [min f]

Category : Math > Optimization and numerical methods
Formula  : Find x that makes f(x) as small as possible

Status   : ready to use - call compute(f, lo, hi)
"""

NAME = 'Minimize'
SYMBOL = 'min f'
CATEGORY = 'Math'
SUBCATEGORY = 'Optimization and numerical methods'
FORMULA = 'Find x that makes f(x) as small as possible'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, lo, hi):
    """x between lo and hi where f is smallest (golden-section search, one hump) → (x, f(x))"""
    g = (math.sqrt(5) - 1) / 2
    a, b = lo, hi
    for _ in range(200):
        c, d = b - g * (b - a), a + g * (b - a)
        if f(c) < f(d):
            b = d
        else:
            a = c
    x = (a + b) / 2
    return x, f(x)
