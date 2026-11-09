"""Magnetic force on a moving charge   [F = qvB sin θ]

Category : Physics > Physics
Formula  : F = q v B sin θ   (θ = angle between v and B, radians)

Status   : ready to use - call compute(q, v, B, theta)
"""
import math

NAME = 'Magnetic force on a moving charge'
SYMBOL = 'F = qvB sin θ'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'F = q v B sin θ   (θ = angle between v and B, radians)'


def compute(q, v, B, theta):
    """F = q v B sin θ   (θ = angle between v and B, radians)"""
    return q * v * B * math.sin(theta)
