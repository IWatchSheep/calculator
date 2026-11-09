"""Limit   [lim]

Category : Math > Calculus
Formula  : lim_{x→a} f(x) = L  means f(x) gets arbitrarily close to L as x gets close to a

Status   : ready to use - call compute(f, a)
"""

NAME = 'Limit'
SYMBOL = 'lim'
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = 'lim_{x→a} f(x) = L  means f(x) gets arbitrarily close to L as x gets close to a'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, a):
    """lim_{x→a} f(x), found numerically from both sides (they must agree)"""
    h = 1e-6
    try:
        left, right = f(a - h), f(a + h)
    except (ZeroDivisionError, ValueError, OverflowError):
        raise ValueError("f is not defined next to a")
    if abs(left - right) > 1e-3 * max(1.0, abs(left), abs(right)):
        raise ValueError("the left and right limits differ (%g and %g)" % (left, right))
    return (left + right) / 2
