"""Magnetic force on a current-carrying wire   [F = BIL sin θ]

Category : Physics > Physics
Formula  : F = B I L sin θ   (θ = angle between wire and B, radians)

Status   : ready to use - call compute(B, I, L, theta)
"""
import math

NAME = 'Magnetic force on a current-carrying wire'
SYMBOL = 'F = BIL sin θ'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'F = B I L sin θ   (θ = angle between wire and B, radians)'


def compute(B, I, L, theta):
    """F = B I L sin θ   (θ = angle between wire and B, radians)"""
    return B * I * L * math.sin(theta)
