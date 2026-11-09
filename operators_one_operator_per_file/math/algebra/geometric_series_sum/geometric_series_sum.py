"""Geometric series sum   [Sₙ]

Category : Math > Algebra
Formula  : Sₙ = a₁(1 − rⁿ) / (1 − r)   (r ≠ 1)

Status   : ready to use - call compute(a1, r, n)
"""

NAME = 'Geometric series sum'
SYMBOL = 'Sₙ'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = 'Sₙ = a₁(1 − rⁿ) / (1 − r)   (r ≠ 1)'


def compute(a1, r, n):
    """Sₙ = a₁(1 − rⁿ) / (1 − r)   (r ≠ 1)"""
    return a1 * n if r == 1 else a1 * (1 - r ** n) / (1 - r)
