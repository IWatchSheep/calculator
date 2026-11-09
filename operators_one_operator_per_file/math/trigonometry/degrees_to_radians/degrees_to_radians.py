"""Degrees to radians   [deg→rad]

Category : Math > Trigonometry
Formula  : radians = degrees × π / 180

Status   : ready to use - call compute(degrees)
"""
import math

NAME = 'Degrees to radians'
SYMBOL = 'deg→rad'
CATEGORY = 'Math'
SUBCATEGORY = 'Trigonometry'
FORMULA = 'radians = degrees × π / 180'


def compute(degrees):
    """radians = degrees × π / 180"""
    return math.radians(degrees)
