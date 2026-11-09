"""Lorentz factor   [γ = 1/√(1 − v²/c²)]

Category : Physics > Physics
Formula  : γ = 1 / √(1 − v²/c²)   (|v| < c)

Status   : ready to use - call compute(v, c)
"""
import math

NAME = 'Lorentz factor'
SYMBOL = 'γ = 1/√(1 − v²/c²)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'γ = 1 / √(1 − v²/c²)   (|v| < c)'


def compute(v, c=299792458):
    """γ = 1 / √(1 − v²/c²)   (|v| < c)"""
    if abs(v) >= c:
        raise ValueError('speed must be less than the speed of light')
    return 1 / math.sqrt(1 - v ** 2 / c ** 2)
