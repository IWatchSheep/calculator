"""Law of sines   [a/sin A = b/sin B]

Category : Geometry > Geometry
Formula  : b = a · sin B / sin A   (angles in radians)

Status   : ready to use - call compute(a, A, B)
"""
import math

NAME = 'Law of sines'
SYMBOL = 'a/sin A = b/sin B'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'b = a · sin B / sin A   (angles in radians)'


def compute(a, A, B):
    """b = a · sin B / sin A   (angles in radians)"""
    return a * math.sin(B) / math.sin(A)
