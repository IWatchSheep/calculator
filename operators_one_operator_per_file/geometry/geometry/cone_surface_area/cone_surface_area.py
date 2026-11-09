"""Cone surface area   [πr(r+l)]

Category : Geometry > Geometry
Formula  : SA = π r (r + l),  l = slant height

Status   : ready to use - call compute(r, l)
"""
import math

NAME = 'Cone surface area'
SYMBOL = 'πr(r+l)'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'SA = π r (r + l),  l = slant height'


def compute(r, l):
    """SA = π r (r + l),  l = slant height"""
    return math.pi * r * (r + l)
