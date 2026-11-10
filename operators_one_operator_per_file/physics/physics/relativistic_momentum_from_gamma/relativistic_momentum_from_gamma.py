"""Relativistic momentum: from the Lorentz factor   [p = γmv]

Category : Physics > Physics
Formula  : p = γ m v   (γ is the answer of the row above)

Status   : ready to use - call compute(gamma, m, v)
"""

NAME = 'Relativistic momentum: from the Lorentz factor'
SYMBOL = 'p = γmv'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'p = γ m v   (γ is the answer of the row above)'


def compute(gamma, m, v):
    """p = γ m v"""
    return m * v * gamma
