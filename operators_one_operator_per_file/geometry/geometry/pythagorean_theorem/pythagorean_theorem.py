"""Pythagorean theorem   [a²+b²=c²]

Category : Geometry > Geometry
Formula  : c = √(a² + b²)   (hypotenuse of a right triangle)

Status   : ready to use - call compute(a, b)
"""
import math

NAME = 'Pythagorean theorem'
SYMBOL = 'a²+b²=c²'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'c = √(a² + b²)   (hypotenuse of a right triangle)'


def compute(a, b):
    """c = √(a² + b²)   (hypotenuse of a right triangle)"""
    return math.hypot(a, b)
