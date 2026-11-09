"""Trace   [tr(A)]

Category : Math > Linear algebra
Formula  : tr(A) = Σᵢ Aᵢᵢ  (sum of the diagonal)

Status   : ready to use - call compute(A)
"""

NAME = 'Trace'
SYMBOL = 'tr(A)'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'tr(A) = Σᵢ Aᵢᵢ  (sum of the diagonal)'


def compute(A):
    """tr(A) = Σᵢ Aᵢᵢ  (sum of the diagonal)"""
    return sum(A[i][i] for i in range(len(A)))
