"""Trapezoid area   [½(a+b)h]

Category : Geometry > Geometry
Formula  : A = ½ (a + b) h

Status   : ready to use - call compute(a, b, h)
"""

NAME = 'Trapezoid area'
SYMBOL = '½(a+b)h'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'A = ½ (a + b) h'


def compute(a, b, h):
    """A = ½ (a + b) h"""
    return 0.5 * (a + b) * h
