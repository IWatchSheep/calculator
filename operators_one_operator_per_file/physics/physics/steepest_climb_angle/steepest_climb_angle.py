"""Steepest climb   [θ = atan μ]

Category : Physics > Physics
Formula  : θ = atan μ   (the steepest slope friction μ can hold, in radians; mass and gravity cancel)

Status   : ready to use - call compute(mu)
"""
import math

NAME = 'Steepest climb'
SYMBOL = 'θ = atan μ'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'θ = atan μ   (the steepest slope friction μ can hold, in radians; mass and gravity cancel)'


def compute(mu):
    """θ = atan μ"""
    if mu < 0:
        raise ValueError("friction cannot be negative")
    return math.atan(mu)
