"""Dimension   [dim V]

Category : Math > Abstract algebra
Formula  : The number of vectors in any basis of V

Status   : ready to use - call compute(vectors)
"""

NAME = 'Dimension'
SYMBOL = 'dim V'
CATEGORY = 'Math'
SUBCATEGORY = 'Abstract algebra'
FORMULA = 'The number of vectors in any basis of V'
import math
from operators_one_operator_per_file import _helpers as H


def compute(vectors):
    """The dimension of the space spanned by the vectors (the rows)"""
    return len(H.rref(vectors)[1])
