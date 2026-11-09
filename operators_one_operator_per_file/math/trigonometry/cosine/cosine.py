"""Cosine   [cos]

Category : Math > Trigonometry
Formula  : cos θ = adjacent / hypotenuse   (θ in radians)

Status   : ready to use - call compute(theta)
"""
import math

NAME = 'Cosine'
SYMBOL = 'cos'
CATEGORY = 'Math'
SUBCATEGORY = 'Trigonometry'
FORMULA = 'cos θ = adjacent / hypotenuse   (θ in radians)'


def compute(theta):
    """cos θ = adjacent / hypotenuse   (θ in radians)"""
    return math.cos(theta)
