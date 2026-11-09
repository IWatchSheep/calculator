"""Simplify   [simplify]

Category : Math > Algebra
Formula  : Rewrite an expression in an equivalent, shorter or standard form

Status   : ready to use - call compute(expr)
"""

NAME = 'Simplify'
SYMBOL = 'simplify'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = 'Rewrite an expression in an equivalent, shorter or standard form'
import math
from operators_one_operator_per_file import _helpers as H


def compute(expr):
    """Simplify a polynomial in x to standard form (collect like terms)"""
    return H.poly_str(H.poly_parse(expr))
