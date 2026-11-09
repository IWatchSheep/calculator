"""Resistors in parallel   [1/R = Σ 1/Rᵢ]

Category : Physics > Physics
Formula  : 1 / R_total = 1/R₁ + 1/R₂ + …

Status   : ready to use - call compute(resistors)
"""

NAME = 'Resistors in parallel'
SYMBOL = '1/R = Σ 1/Rᵢ'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = '1 / R_total = 1/R₁ + 1/R₂ + …'


def compute(resistors):
    """1 / R_total = 1/R₁ + 1/R₂ + …"""
    return 1 / sum(1 / r for r in resistors)
