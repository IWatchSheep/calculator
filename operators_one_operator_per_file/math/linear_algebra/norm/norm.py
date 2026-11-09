"""Norm   [‖v‖ₚ]

Category : Math > Linear algebra
Formula  : ‖v‖ₚ = (Σ |vᵢ|ᵖ)^(1/p)

Status   : ready to use - call compute(v, p=2)
"""

NAME = 'Norm'
SYMBOL = '‖v‖ₚ'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = '‖v‖ₚ = (Σ |vᵢ|ᵖ)^(1/p)'


def compute(v, p=2):
    """‖v‖ₚ = (Σ |vᵢ|ᵖ)^(1/p)"""
    return sum(abs(x) ** p for x in v) ** (1 / p)
