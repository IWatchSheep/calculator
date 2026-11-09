"""Eigenvalues   [λ]

Category : Math > Linear algebra
Formula  : det(A − λI) = 0   (closed form for a 2×2 matrix: λ = (tr ± √(tr² − 4·det)) / 2)

Status   : ready to use - call compute(A)
"""
import cmath

NAME = 'Eigenvalues'
SYMBOL = 'λ'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'det(A − λI) = 0   (closed form for a 2×2 matrix: λ = (tr ± √(tr² − 4·det)) / 2)'


def compute(A):
    """det(A − λI) = 0   (closed form for a 2×2 matrix: λ = (tr ± √(tr² − 4·det)) / 2)"""
    tr = A[0][0] + A[1][1]
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    root = cmath.sqrt(tr * tr - 4 * det)
    return ((tr + root) / 2, (tr - root) / 2)
