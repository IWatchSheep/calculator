"""Solve system of equations   [system]

Category : Math > Algebra
Formula  : Find values satisfying several equations at once; for linear systems solve Ax = b

Status   : ready to use - call compute(A, b)
"""

NAME = 'Solve system of equations'
SYMBOL = 'system'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = 'Find values satisfying several equations at once; for linear systems solve Ax = b'
import math
from operators_one_operator_per_file import _helpers as H


def compute(A, b):
    """Solve A·x = b for a square system with one solution"""
    n = len(A)
    R, piv = H.rref([list(row) + [bi] for row, bi in zip(A, b)])
    if piv != list(range(n)):
        raise ValueError("the system has no single solution")
    return [R[i][n] for i in range(n)]
