"""Cylinder surface area   [2πr(r+h)]

Category : Geometry > Geometry
Formula  : SA = 2 π r (r + h)

Status   : ready to use - call compute(r, h)
"""
import math

NAME = 'Cylinder surface area'
SYMBOL = '2πr(r+h)'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'SA = 2 π r (r + h)'


def compute(r, h):
    """SA = 2 π r (r + h)"""
    return 2 * math.pi * r * (r + h)
