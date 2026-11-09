"""Radians to degrees   [rad→deg]

Category : Math > Trigonometry
Formula  : degrees = radians × 180 / π

Status   : ready to use - call compute(radians)
"""
import math

NAME = 'Radians to degrees'
SYMBOL = 'rad→deg'
CATEGORY = 'Math'
SUBCATEGORY = 'Trigonometry'
FORMULA = 'degrees = radians × 180 / π'


def compute(radians):
    """degrees = radians × 180 / π"""
    return math.degrees(radians)
