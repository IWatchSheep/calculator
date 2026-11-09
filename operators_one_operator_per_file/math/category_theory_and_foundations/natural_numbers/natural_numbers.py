"""Natural numbers   [ℕ]

Category : Math > Category theory and foundations
Formula  : {0, 1, 2, 3, …} (or {1, 2, 3, …})

Status   : ready to use - call compute(x)
"""

NAME = 'Natural numbers'
SYMBOL = 'ℕ'
CATEGORY = 'Math'
SUBCATEGORY = 'Category theory and foundations'
FORMULA = '{0, 1, 2, 3, …} (or {1, 2, 3, …})'
import math
from operators_one_operator_per_file import _helpers as H


def compute(x):
    """True if x is a natural number (0, 1, 2, 3, …)"""
    return float(x).is_integer() and x >= 0
