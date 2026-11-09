"""LU decomposition   [A = LU]

Category : Math > Linear algebra
Formula  : A = L·U with L lower-triangular and U upper-triangular

Status   : ready to use - call compute(A)
"""

NAME = 'LU decomposition'
SYMBOL = 'A = LU'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'A = L·U with L lower-triangular and U upper-triangular'
import math
from operators_one_operator_per_file import _helpers as H


def compute(A):
    """A = L·U  (Doolittle, no row swaps) → (L, U)"""
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for k in range(i, n):
            U[i][k] = A[i][k] - sum(L[i][j] * U[j][k] for j in range(i))
        for k in range(i, n):
            if i == k:
                L[i][i] = 1.0
            else:
                if abs(U[i][i]) < 1e-12:
                    raise ValueError("a zero pivot: this matrix needs row swaps")
                L[k][i] = (A[k][i] - sum(L[k][j] * U[j][i] for j in range(i))) / U[i][i]
    return L, U
