"""Relativistic kinetic energy   [K = (γ − 1)mc²]

Category : Physics > Physics
Formula  : K = (γ − 1) m c²   (γ = 1/√(1 − v²/c²))

Status   : ready to use - call compute(m, v, c)
"""
import math

NAME = 'Relativistic kinetic energy'
SYMBOL = 'K = (γ − 1)mc²'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'K = (γ − 1) m c²   (γ = 1/√(1 − v²/c²))'


def compute(m, v, c=299792458):
    """K = (γ − 1) m c²   (γ = 1/√(1 − v²/c²))"""
    if abs(v) >= c:
        raise ValueError('speed must be less than the speed of light')
    return (1 / math.sqrt(1 - v ** 2 / c ** 2) - 1) * m * c ** 2
