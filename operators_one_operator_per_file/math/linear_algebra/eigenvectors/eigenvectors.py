"""Eigenvectors   [v]

Category : Math > Linear algebra
Formula  : A·v = λ·v  — solve (A − λI)v = 0 for v ≠ 0 for each eigenvalue λ

Status   : ready to use - call compute(A)
"""

NAME = 'Eigenvectors'
SYMBOL = 'v'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'A·v = λ·v  — solve (A − λI)v = 0 for v ≠ 0 for each eigenvalue λ'
import math
from operators_one_operator_per_file import _helpers as H


def compute(A):
    """Eigenvalues with their eigenvectors: [(λ, [v1, v2, …]), …]  (2×2 or symmetric matrices)"""
    n = len(A)
    if n == 2:
        tr, det = A[0][0] + A[1][1], A[0][0] * A[1][1] - A[0][1] * A[1][0]
        disc = tr * tr / 4 - det
        if disc < -1e-12:
            raise ValueError("the eigenvalues are complex")
        s = math.sqrt(max(disc, 0))
        vals = sorted({round(tr / 2 + s, 10), round(tr / 2 - s, 10)}, reverse=True)
    elif all(abs(A[i][j] - A[j][i]) < 1e-12 for i in range(n) for j in range(n)):
        vals = sorted({round(v, 8) for v in H.jacobi_eigen(A)}, reverse=True)
    else:
        raise ValueError("only 2×2 or symmetric matrices")
    out = []
    for lam in vals:
        shifted = [[A[i][j] - (lam if i == j else 0) for j in range(n)] for i in range(n)]
        vecs = H.nullspace(shifted)
        out.append((lam, [[round(c, 10) for c in v] for v in vecs]))
    return out
