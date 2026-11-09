"""Convex function   [convex]

Category : Math > Optimization and numerical methods
Formula  : f(tx + (1−t)y) ≤ t·f(x) + (1−t)·f(y) for t in [0, 1]

Status   : ready to use - call compute(f, x, y)
"""

NAME = 'Convex function'
SYMBOL = 'convex'
CATEGORY = 'Math'
SUBCATEGORY = 'Optimization and numerical methods'
FORMULA = 'f(tx + (1−t)y) ≤ t·f(x) + (1−t)·f(y) for t in [0, 1]'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, x, y):
    """Checks f(tx + (1−t)y) ≤ t·f(x) + (1−t)·f(y) for 101 values of t in [0, 1]  → True / False"""
    for k in range(101):
        t = k / 100
        if f(t * x + (1 - t) * y) > t * f(x) + (1 - t) * f(y) + 1e-9:
            return False
    return True
