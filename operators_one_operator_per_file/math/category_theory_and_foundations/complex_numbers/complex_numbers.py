"""Complex numbers   [ℂ]

Category : Math > Category theory and foundations
Formula  : { a + bi : a, b ∈ ℝ }

Status   : ready to use - call compute(a, b)
"""

NAME = 'Complex numbers'
SYMBOL = 'ℂ'
CATEGORY = 'Math'
SUBCATEGORY = 'Category theory and foundations'
FORMULA = '{ a + bi : a, b ∈ ℝ }'
import math
from operators_one_operator_per_file import _helpers as H


def compute(a, b):
    """The complex number a + bi"""
    return complex(a, b)
