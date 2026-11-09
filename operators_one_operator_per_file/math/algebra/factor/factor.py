"""Factor   [factor]

Category : Math > Algebra
Formula  : Rewrite a polynomial as a product of lower-degree polynomials, e.g. x² − 1 = (x − 1)(x + 1)

Status   : ready to use - call compute(expr)
"""

NAME = 'Factor'
SYMBOL = 'factor'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = 'Rewrite a polynomial as a product of lower-degree polynomials, e.g. x² − 1 = (x − 1)(x + 1)'
import math
from operators_one_operator_per_file import _helpers as H


def compute(expr):
    """Factor a polynomial in x using rational roots, e.g. x^2 - 1 → (x - 1) (x + 1)"""
    return H.poly_factor(H.poly_parse(expr))
