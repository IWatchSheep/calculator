"""Transpose   [Aᵀ]

Category : Math > Linear algebra
Formula  : (Aᵀ)ᵢⱼ = Aⱼᵢ

Status   : ready to use - call compute(A)
"""

NAME = 'Transpose'
SYMBOL = 'Aᵀ'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = '(Aᵀ)ᵢⱼ = Aⱼᵢ'


def compute(A):
    """(Aᵀ)ᵢⱼ = Aⱼᵢ"""
    return [list(r) for r in zip(*A)]
