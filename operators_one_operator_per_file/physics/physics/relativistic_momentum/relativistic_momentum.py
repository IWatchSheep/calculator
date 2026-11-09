"""Relativistic momentum   [p = γmv]

Category : Physics > Physics
Formula  : p = m v / √(1 − v²/c²)

Status   : ready to use - call compute(m, v, c)
"""
import math

NAME = 'Relativistic momentum'
SYMBOL = 'p = γmv'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'p = m v / √(1 − v²/c²)'


def compute(m, v, c=299792458):
    """p = m v / √(1 − v²/c²)"""
    if abs(v) >= c:
        raise ValueError('speed must be less than the speed of light')
    return m * v / math.sqrt(1 - v ** 2 / c ** 2)
