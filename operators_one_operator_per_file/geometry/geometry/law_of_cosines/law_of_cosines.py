"""Law of cosines   [c²=a²+b²−2ab·cos C]

Category : Geometry > Geometry
Formula  : c = √(a² + b² − 2ab cos C)   (C in radians)

Status   : ready to use - call compute(a, b, C)
"""
import math

NAME = 'Law of cosines'
SYMBOL = 'c²=a²+b²−2ab·cos C'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'c = √(a² + b² − 2ab cos C)   (C in radians)'


def compute(a, b, C):
    """c = √(a² + b² − 2ab cos C)   (C in radians)"""
    return math.sqrt(a * a + b * b - 2 * a * b * math.cos(C))
