"""Slope   [(y₂−y₁)/(x₂−x₁)]

Category : Geometry > Geometry
Formula  : m = (y₂ − y₁) / (x₂ − x₁)

Status   : ready to use - call compute(x1, y1, x2, y2)
"""

NAME = 'Slope'
SYMBOL = '(y₂−y₁)/(x₂−x₁)'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'm = (y₂ − y₁) / (x₂ − x₁)'


def compute(x1, y1, x2, y2):
    """m = (y₂ − y₁) / (x₂ − x₁)"""
    return (y2 - y1) / (x2 - x1)
