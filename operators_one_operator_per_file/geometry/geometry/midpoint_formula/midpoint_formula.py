"""Midpoint formula   [((x₁+x₂)/2, (y₁+y₂)/2)]

Category : Geometry > Geometry
Formula  : M = ((x₁ + x₂)/2, (y₁ + y₂)/2)

Status   : ready to use - call compute(x1, y1, x2, y2)
"""

NAME = 'Midpoint formula'
SYMBOL = '((x₁+x₂)/2, (y₁+y₂)/2)'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'M = ((x₁ + x₂)/2, (y₁ + y₂)/2)'


def compute(x1, y1, x2, y2):
    """M = ((x₁ + x₂)/2, (y₁ + y₂)/2)"""
    return ((x1 + x2) / 2, (y1 + y2) / 2)
