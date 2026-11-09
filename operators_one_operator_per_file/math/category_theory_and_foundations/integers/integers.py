"""Integers   [ℤ]

Category : Math > Category theory and foundations
Formula  : {…, −2, −1, 0, 1, 2, …}

Status   : ready to use - call compute(x)
"""

NAME = 'Integers'
SYMBOL = 'ℤ'
CATEGORY = 'Math'
SUBCATEGORY = 'Category theory and foundations'
FORMULA = '{…, −2, −1, 0, 1, 2, …}'
import math
from operators_one_operator_per_file import _helpers as H


def compute(x):
    """True if x is an integer"""
    return float(x).is_integer()
