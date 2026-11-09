"""Arithmetic sequence   [aₙ]

Category : Math > Algebra
Formula  : aₙ = a₁ + (n − 1)d

Status   : ready to use - call compute(a1, d, n)
"""

NAME = 'Arithmetic sequence'
SYMBOL = 'aₙ'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = 'aₙ = a₁ + (n − 1)d'


def compute(a1, d, n):
    """aₙ = a₁ + (n − 1)d"""
    return a1 + (n - 1) * d
