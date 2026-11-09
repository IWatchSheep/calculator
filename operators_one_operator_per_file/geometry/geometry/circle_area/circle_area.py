"""Circle area   [πr²]

Category : Geometry > Geometry
Formula  : A = π r²

Status   : ready to use - call compute(r)
"""
import math

NAME = 'Circle area'
SYMBOL = 'πr²'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'A = π r²'


def compute(r):
    """A = π r²"""
    return math.pi * r ** 2
