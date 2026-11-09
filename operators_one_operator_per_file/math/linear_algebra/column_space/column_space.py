"""Column space   [col(A)]

Category : Math > Linear algebra
Formula  : col(A) = span of the columns of A = { A·x : x }

Status   : ready to use - call compute(A)
"""

NAME = 'Column space'
SYMBOL = 'col(A)'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'col(A) = span of the columns of A = { A·x : x }'
import math
from operators_one_operator_per_file import _helpers as H


def compute(A):
    """col(A): a basis made of the pivot columns of A"""
    _R, piv = H.rref(A)
    cols = H.transpose(A)
    return [list(cols[p]) for p in piv]
