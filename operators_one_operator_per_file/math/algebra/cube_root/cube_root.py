"""Cube root   [∛]

Category : Math > Algebra
Formula  : ∛x  (y such that y³ = x)

Status   : ready to use - call compute(x)
"""
import math

NAME = 'Cube root'
SYMBOL = '∛'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = '∛x  (y such that y³ = x)'


def compute(x):
    """∛x  (y such that y³ = x)"""
    return math.copysign(abs(x) ** (1 / 3), x)
