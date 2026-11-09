"""Relativistic Doppler effect   [f = f₀√((1−β)/(1+β))]

Category : Physics > Physics
Formula  : f = f₀ √( (1 − β)/(1 + β) ),  β = v/c   (v > 0 receding, v < 0 approaching)

Status   : ready to use - call compute(f0, v, c)
"""
import math

NAME = 'Relativistic Doppler effect'
SYMBOL = 'f = f₀√((1−β)/(1+β))'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'f = f₀ √( (1 − β)/(1 + β) ),  β = v/c   (v > 0 receding, v < 0 approaching)'


def compute(f0, v, c=299792458):
    """f = f₀ √( (1 − β)/(1 + β) ),  β = v/c   (v > 0 receding, v < 0 approaching)"""
    if abs(v) >= c:
        raise ValueError('speed must be less than the speed of light')
    beta = v / c
    return f0 * math.sqrt((1 - beta) / (1 + beta))
