"""Exponential smoothing   [y = αx + (1 − α)y₀]

Category : Physics > Physics
Formula  : y = α x + (1 − α) y₀   (one new sample blended into the previous estimate; α = 0 keeps the old value, α = 1 takes the new sample)

Status   : ready to use - call compute(previous, sample, alpha)
"""
import math

NAME = 'Exponential smoothing'
SYMBOL = 'y = αx + (1 − α)y₀'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'y = α x + (1 − α) y₀   (one new sample blended into the previous estimate; α = 0 keeps the old value, α = 1 takes the new sample)'


def compute(previous, sample, alpha):
    """y = α x + (1 − α) y₀"""
    if not 0 <= alpha <= 1:
        raise ValueError("the weight must be from 0 to 1")
    return alpha * sample + (1 - alpha) * previous
