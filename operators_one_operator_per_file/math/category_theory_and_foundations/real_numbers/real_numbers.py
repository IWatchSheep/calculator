"""Real numbers   [ℝ]

Category : Math > Category theory and foundations
Formula  : The complete ordered field: all rational and irrational numbers

Status   : ready to use - call compute(x)
"""

NAME = 'Real numbers'
SYMBOL = 'ℝ'
CATEGORY = 'Math'
SUBCATEGORY = 'Category theory and foundations'
FORMULA = 'The complete ordered field: all rational and irrational numbers'
import math
from operators_one_operator_per_file import _helpers as H


def compute(x):
    """True: every number you can type is a real number"""
    return True
