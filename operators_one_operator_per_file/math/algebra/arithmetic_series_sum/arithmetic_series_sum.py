"""Arithmetic series sum   [Sₙ]

Category : Math > Algebra
Formula  : Sₙ = n/2 · (2a₁ + (n − 1)d)

Status   : ready to use - call compute(a1, d, n)
"""

NAME = 'Arithmetic series sum'
SYMBOL = 'Sₙ'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = 'Sₙ = n/2 · (2a₁ + (n − 1)d)'


def compute(a1, d, n):
    """Sₙ = n/2 · (2a₁ + (n − 1)d)"""
    return n / 2 * (2 * a1 + (n - 1) * d)
