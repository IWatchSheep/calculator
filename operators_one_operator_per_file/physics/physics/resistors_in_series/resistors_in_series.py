"""Resistors in series   [R₁+R₂+…]

Category : Physics > Physics
Formula  : R_total = R₁ + R₂ + …

Status   : ready to use - call compute(resistors)
"""

NAME = 'Resistors in series'
SYMBOL = 'R₁+R₂+…'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'R_total = R₁ + R₂ + …'


def compute(resistors):
    """R_total = R₁ + R₂ + …"""
    return sum(resistors)
