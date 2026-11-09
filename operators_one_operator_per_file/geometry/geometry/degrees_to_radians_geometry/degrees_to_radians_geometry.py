"""Degrees to radians (Geometry)   [deg→rad]

Category : Geometry > Geometry
Formula  : radians = degrees × π / 180

Status   : ready to use - call compute(degrees)
"""
import math

NAME = 'Degrees to radians (Geometry)'
SYMBOL = 'deg→rad'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'radians = degrees × π / 180'


def compute(degrees):
    """radians = degrees × π / 180"""
    return math.radians(degrees)
