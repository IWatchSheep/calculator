"""Sphere surface area   [4πr²]

Category : Geometry > Geometry
Formula  : SA = 4 π r²

Status   : ready to use - call compute(r)
"""
import math

NAME = 'Sphere surface area'
SYMBOL = '4πr²'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'SA = 4 π r²'


def compute(r):
    """SA = 4 π r²"""
    return 4 * math.pi * r ** 2
