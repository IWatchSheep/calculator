"""Rectangular prism volume   [lwh]

Category : Geometry > Geometry
Formula  : V = l · w · h

Status   : ready to use - call compute(l, w, h)
"""

NAME = 'Rectangular prism volume'
SYMBOL = 'lwh'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'V = l · w · h'


def compute(l, w, h):
    """V = l · w · h"""
    return l * w * h
