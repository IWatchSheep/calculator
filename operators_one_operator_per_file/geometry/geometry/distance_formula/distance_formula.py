"""Distance formula   [√((x₂−x₁)²+(y₂−y₁)²)]

Category : Geometry > Geometry
Formula  : d = √((x₂ − x₁)² + (y₂ − y₁)²)

Status   : ready to use - call compute(x1, y1, x2, y2)
"""
import math

NAME = 'Distance formula'
SYMBOL = '√((x₂−x₁)²+(y₂−y₁)²)'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'd = √((x₂ − x₁)² + (y₂ − y₁)²)'


def compute(x1, y1, x2, y2):
    """d = √((x₂ − x₁)² + (y₂ − y₁)²)"""
    return math.dist((x1, y1), (x2, y2))
