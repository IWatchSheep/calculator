"""L'Hopital's rule   [L'H]

Category : Math > Calculus
Formula  : If lim f/g is 0/0 or ∞/∞ then lim f/g = lim f′/g′  (when that limit exists)

Status   : ready to use - call compute(f, g, a)
"""

NAME = "L'Hopital's rule"
SYMBOL = "L'H"
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = 'If lim f/g is 0/0 or ∞/∞ then lim f/g = lim f′/g′  (when that limit exists)'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, g, a):
    """lim f/g = lim f′/g′  (numerical derivatives, both sides of a)"""
    def d(F, x, h=1e-5):
        return (F(x + h) - F(x - h)) / (2 * h)
    h = 1e-4
    left = d(f, a - h) / d(g, a - h)
    right = d(f, a + h) / d(g, a + h)
    if abs(left - right) > 1e-2 * max(1.0, abs(left), abs(right)):
        raise ValueError("the one-sided limits of f′/g′ differ")
    return (left + right) / 2
