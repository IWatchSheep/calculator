"""Relativistic kinetic energy: from the Lorentz factor   [K = (γ − 1)mc²]

Category : Physics > Physics
Formula  : K = (γ − 1) m c²   (γ is the answer of the row above)

Status   : ready to use - call compute(gamma, m, c=299792458)
"""

NAME = 'Relativistic kinetic energy: from the Lorentz factor'
SYMBOL = 'K = (γ − 1)mc²'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'K = (γ − 1) m c²   (γ is the answer of the row above)'


def compute(gamma, m, c=299792458):
    """K = (γ − 1) m c²"""
    return (gamma - 1) * m * c ** 2
