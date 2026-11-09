"""Null space   [null(A)]

Category : Math > Linear algebra
Formula  : null(A) = { x : A·x = 0 }

Status   : ready to use - call compute(A)
"""

NAME = 'Null space'
SYMBOL = 'null(A)'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'null(A) = { x : A·x = 0 }'
import math
from operators_one_operator_per_file import _helpers as H


def compute(A):
    """null(A) = { x : A·x = 0 }  (a basis, as a list of vectors; [] if only x = 0)"""
    return [[round(c, 10) for c in v] for v in H.nullspace(A)]
