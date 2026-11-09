"""Rational numbers   [ℚ]

Category : Math > Category theory and foundations
Formula  : { p/q : p, q ∈ ℤ, q ≠ 0 }

Status   : ready to use - call compute(p, q)
"""

NAME = 'Rational numbers'
SYMBOL = 'ℚ'
CATEGORY = 'Math'
SUBCATEGORY = 'Category theory and foundations'
FORMULA = '{ p/q : p, q ∈ ℤ, q ≠ 0 }'
import math
from operators_one_operator_per_file import _helpers as H


def compute(p, q):
    """The rational number p/q (q ≠ 0), as a decimal"""
    if q == 0:
        raise ValueError("q can't be 0")
    return p / q
