"""Sphere volume   [⁴⁄₃πr³]

Category : Geometry > Geometry
Formula  : V = 4/3 π r³

Status   : ready to use - call compute(r)
"""
import math

NAME = 'Sphere volume'
SYMBOL = '⁴⁄₃πr³'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'V = 4/3 π r³'


def compute(r):
    """V = 4/3 π r³"""
    return 4 / 3 * math.pi * r ** 3
