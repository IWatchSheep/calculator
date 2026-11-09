"""Characteristic polynomial   [p(λ)]

Category : Math > Linear algebra
Formula  : p(λ) = det(A − λI);  for 2×2: λ² − tr(A)·λ + det(A)  (returns [1, −tr, det])

Status   : ready to use - call compute(A)
"""

NAME = 'Characteristic polynomial'
SYMBOL = 'p(λ)'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'p(λ) = det(A − λI);  for 2×2: λ² − tr(A)·λ + det(A)  (returns [1, −tr, det])'


def compute(A):
    """p(λ) = det(A − λI);  for 2×2: λ² − tr(A)·λ + det(A)  (returns [1, −tr, det])"""
    return [1, -(A[0][0] + A[1][1]), A[0][0] * A[1][1] - A[0][1] * A[1][0]]
