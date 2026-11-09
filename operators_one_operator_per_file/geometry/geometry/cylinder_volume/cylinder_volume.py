"""Cylinder volume   [πr²h]

Category : Geometry > Geometry
Formula  : V = π r² h

Status   : ready to use - call compute(r, h)
"""
import math

NAME = 'Cylinder volume'
SYMBOL = 'πr²h'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'V = π r² h'


def compute(r, h):
    """V = π r² h"""
    return math.pi * r ** 2 * h
