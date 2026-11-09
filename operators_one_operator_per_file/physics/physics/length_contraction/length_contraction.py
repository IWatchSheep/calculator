"""Length contraction   [L = L₀/γ]

Category : Physics > Physics
Formula  : L = L₀ √(1 − v²/c²)   (L₀ = length at rest)

Status   : ready to use - call compute(L0, v, c)
"""
import math

NAME = 'Length contraction'
SYMBOL = 'L = L₀/γ'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'L = L₀ √(1 − v²/c²)   (L₀ = length at rest)'


def compute(L0, v, c=299792458):
    """L = L₀ √(1 − v²/c²)   (L₀ = length at rest)"""
    if abs(v) >= c:
        raise ValueError('speed must be less than the speed of light')
    return L0 * math.sqrt(1 - v ** 2 / c ** 2)
