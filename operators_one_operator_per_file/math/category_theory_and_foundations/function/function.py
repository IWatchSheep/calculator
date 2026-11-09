"""Function   [f: A → B]

Category : Math > Category theory and foundations
Formula  : A rule assigning to each element of A exactly one element of B

Status   : ready to use - call compute(f, x)
"""

NAME = 'Function'
SYMBOL = 'f: A → B'
CATEGORY = 'Math'
SUBCATEGORY = 'Category theory and foundations'
FORMULA = 'A rule assigning to each element of A exactly one element of B'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, x):
    """The value f(x) of a rule f at x"""
    return f(x)
