"""Cone volume   [⅓πr²h]

Category : Geometry > Geometry
Formula  : V = ⅓ π r² h

Status   : ready to use - call compute(r, h)
"""
import math

NAME = 'Cone volume'
SYMBOL = '⅓πr²h'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'V = ⅓ π r² h'


def compute(r, h):
    """V = ⅓ π r² h"""
    return math.pi * r ** 2 * h / 3
