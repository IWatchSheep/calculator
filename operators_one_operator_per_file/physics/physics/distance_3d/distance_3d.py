"""Distance in 3D   [|b − a|]

Category : Physics > Physics
Formula  : |b − a|   (the straight-line distance between two points, in metres)

Status   : ready to use - call compute(a, b)
"""
import math

NAME = 'Distance in 3D'
SYMBOL = '|b − a|'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = '|b − a|   (the straight-line distance between two points, in metres)'


def compute(a, b):
    """the straight-line distance between two points [x, y, z]"""
    if len(a) != 3 or len(b) != 3:
        raise ValueError("a point has 3 numbers: x, y, z")
    dx, dy, dz = b[0] - a[0], b[1] - a[1], b[2] - a[2]
    return math.sqrt(dx * dx + dy * dy + dz * dz)
