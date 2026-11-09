"""Singular value decomposition   [SVD]

Category : Math > Linear algebra
Formula  : A = U·Σ·Vᵀ with U, V orthogonal and Σ diagonal of singular values

Status   : ready to use - call compute(A)
"""

NAME = 'Singular value decomposition'
SYMBOL = 'SVD'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'A = U·Σ·Vᵀ with U, V orthogonal and Σ diagonal of singular values'
import math
from operators_one_operator_per_file import _helpers as H


def compute(A):
    """The singular values of A (square roots of the eigenvalues of AᵀA), largest first"""
    ata = H.matmul(H.transpose(A), A)
    return [math.sqrt(max(v, 0.0)) for v in H.jacobi_eigen(ata)]
