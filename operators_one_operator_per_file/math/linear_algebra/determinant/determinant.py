"""Determinant   [det(A)]

Category : Math > Linear algebra
Formula  : det(A) = Σⱼ (−1)ʲ · A₀ⱼ · det(minor₀ⱼ)   (cofactor expansion along row 0)

Status   : ready to use - call compute(A)
"""

NAME = 'Determinant'
SYMBOL = 'det(A)'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'det(A) = Σⱼ (−1)ʲ · A₀ⱼ · det(minor₀ⱼ)   (cofactor expansion along row 0)'


def compute(A):
    """det(A) = Σⱼ (−1)ʲ · A₀ⱼ · det(minor₀ⱼ)   (cofactor expansion along row 0)"""
    n = len(A)
    if n == 1:
        return A[0][0]
    return sum((-1) ** j * A[0][j] * compute([row[:j] + row[j + 1:] for row in A[1:]]) for j in range(n))
