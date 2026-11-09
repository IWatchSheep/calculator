"""Geometric sequence   [aₙ]

Category : Math > Algebra
Formula  : aₙ = a₁ · rⁿ⁻¹

Status   : ready to use - call compute(a1, r, n)
"""

NAME = 'Geometric sequence'
SYMBOL = 'aₙ'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = 'aₙ = a₁ · rⁿ⁻¹'


def compute(a1, r, n):
    """aₙ = a₁ · rⁿ⁻¹"""
    return a1 * r ** (n - 1)
