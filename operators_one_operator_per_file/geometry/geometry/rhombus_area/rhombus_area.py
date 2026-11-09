"""Rhombus area   [½d₁d₂]

Category : Geometry > Geometry
Formula  : A = ½ d₁ d₂

Status   : ready to use - call compute(d1, d2)
"""

NAME = 'Rhombus area'
SYMBOL = '½d₁d₂'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'A = ½ d₁ d₂'


def compute(d1, d2):
    """A = ½ d₁ d₂"""
    return 0.5 * d1 * d2
