"""Sine   [sin]

Category : Math > Trigonometry
Formula  : sin θ = opposite / hypotenuse   (θ in radians)

Status   : ready to use - call compute(theta)
"""
import math

NAME = 'Sine'
SYMBOL = 'sin'
CATEGORY = 'Math'
SUBCATEGORY = 'Trigonometry'
FORMULA = 'sin θ = opposite / hypotenuse   (θ in radians)'


def compute(theta):
    """sin θ = opposite / hypotenuse   (θ in radians)"""
    return math.sin(theta)
