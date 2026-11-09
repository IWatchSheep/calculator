"""Radians to degrees (Geometry)   [rad→deg]

Category : Geometry > Geometry
Formula  : degrees = radians × 180 / π

Status   : ready to use - call compute(radians)
"""
import math

NAME = 'Radians to degrees (Geometry)'
SYMBOL = 'rad→deg'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'degrees = radians × 180 / π'


def compute(radians):
    """degrees = radians × 180 / π"""
    return math.degrees(radians)
