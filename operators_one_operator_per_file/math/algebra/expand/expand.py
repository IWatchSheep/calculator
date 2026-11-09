"""Expand   [expand]

Category : Math > Algebra
Formula  : Multiply out products, e.g. (x + 1)(x − 1) = x² − 1

Status   : ready to use - call compute(expr)
"""

NAME = 'Expand'
SYMBOL = 'expand'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = 'Multiply out products, e.g. (x + 1)(x − 1) = x² − 1'
import math
from operators_one_operator_per_file import _helpers as H


def compute(expr):
    """Multiply out a polynomial in x, e.g. (x+1)(x-1) → x² − 1"""
    return H.poly_str(H.poly_parse(expr))
