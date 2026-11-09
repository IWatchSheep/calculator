"""Summation   [Σ]

Category : Math > Calculus
Formula  : Σ aᵢ = a₁ + a₂ + … + aₙ

Status   : ready to use - call compute(terms)
"""

NAME = 'Summation'
SYMBOL = 'Σ'
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = 'Σ aᵢ = a₁ + a₂ + … + aₙ'


def compute(terms):
    """Σ aᵢ = a₁ + a₂ + … + aₙ"""
    return sum(terms)
