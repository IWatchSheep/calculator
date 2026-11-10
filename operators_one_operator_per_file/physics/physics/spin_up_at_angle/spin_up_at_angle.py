"""Spin up at an angle   [P = (1 + cos θ) / 2]

Category : Physics > Physics
Formula  : P = (1 + cos θ) / 2 = cos²(θ/2)   (a spin-1/2 particle prepared spin up along z is found spin up along an axis at angle θ from z, in radians; the (1 + cos θ) / 2 form makes 90° exactly 0.5 and 180° exactly 0)

Status   : ready to use - call compute(theta)
"""
import math

NAME = 'Spin up at an angle'
SYMBOL = 'P = (1 + cos θ) / 2'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'P = (1 + cos θ) / 2 = cos²(θ/2)   (a spin-1/2 particle prepared spin up along z is found spin up along an axis at angle θ from z, in radians; the (1 + cos θ) / 2 form makes 90° exactly 0.5 and 180° exactly 0)'


def compute(theta):
    """probability, from 0 to 1"""
    return (1 + math.cos(theta)) / 2
