"""Circle circumference   [2πr]

Category : Geometry > Geometry
Formula  : C = 2 π r

Status   : ready to use - call compute(r)
"""
import math

NAME = 'Circle circumference'
SYMBOL = '2πr'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'C = 2 π r'


def compute(r):
    """C = 2 π r"""
    return 2 * math.pi * r
