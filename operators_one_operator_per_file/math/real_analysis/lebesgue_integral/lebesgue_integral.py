"""Lebesgue integral   [∫ f dμ]

Category : Math > Real analysis
Formula  : Integral defined by approximating f with simple functions and measuring their level sets

Status   : ready to use - call compute(f, a, b)
"""

NAME = 'Lebesgue integral'
SYMBOL = '∫ f dμ'
CATEGORY = 'Math'
SUBCATEGORY = 'Real analysis'
FORMULA = 'Integral defined by approximating f with simple functions and measuring their level sets'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, a, b):
    """∫ f dμ over [a, b] for a well-behaved f  (numerical: Simpson's rule)"""
    return H.simpson(f, a, b, 2000)
