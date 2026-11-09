"""Magnetic flux   [Φ = BA cos θ]

Category : Physics > Physics
Formula  : Φ = B A cos θ   (θ = angle between B and the surface normal, radians)

Status   : ready to use - call compute(B, A, theta)
"""
import math

NAME = 'Magnetic flux'
SYMBOL = 'Φ = BA cos θ'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'Φ = B A cos θ   (θ = angle between B and the surface normal, radians)'


def compute(B, A, theta):
    """Φ = B A cos θ   (θ = angle between B and the surface normal, radians)"""
    return B * A * math.cos(theta)
