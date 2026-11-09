"""Inverse tangent   [atan]

Category : Math > Trigonometry
Formula  : θ = arctan(x)

Status   : ready to use - call compute(x)
"""
import math

NAME = 'Inverse tangent'
SYMBOL = 'atan'
CATEGORY = 'Math'
SUBCATEGORY = 'Trigonometry'
FORMULA = 'θ = arctan(x)'


def compute(x):
    """θ = arctan(x)"""
    return math.atan(x)
