"""Product   [∏]

Category : Math > Calculus
Formula  : ∏ aᵢ = a₁ · a₂ · … · aₙ

Status   : ready to use - call compute(terms)
"""
import math

NAME = 'Product'
SYMBOL = '∏'
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = '∏ aᵢ = a₁ · a₂ · … · aₙ'


def compute(terms):
    """∏ aᵢ = a₁ · a₂ · … · aₙ"""
    return math.prod(terms)
