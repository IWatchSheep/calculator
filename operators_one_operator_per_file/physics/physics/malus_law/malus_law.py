"""Malus's law   [I = I₀cos²θ]

Category : Physics > Physics
Formula  : I = I₀ cos²θ   (θ = angle between polariser axes, radians)

Status   : ready to use - call compute(I0, theta)
"""
import math

NAME = "Malus's law"
SYMBOL = 'I = I₀cos²θ'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'I = I₀ cos²θ   (θ = angle between polariser axes, radians)'


def compute(I0, theta):
    """I = I₀ cos²θ   (θ = angle between polariser axes, radians)"""
    return I0 * math.cos(theta) ** 2
