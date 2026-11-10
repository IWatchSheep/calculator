"""Point inside a sphere   [|p − c| ≤ R]

Category : Physics > Physics
Formula  : 1 if the point is inside or on the sphere, 0 if it is outside

Status   : ready to use - call compute(centre, radius, point)
"""
import math

NAME = 'Point inside a sphere'
SYMBOL = '|p − c| ≤ R'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = '1 if the point is inside or on the sphere, 0 if it is outside'


def compute(centre, radius, point):
    """1 if the point is inside or on the sphere, 0 if outside"""
    if len(centre) != 3 or len(point) != 3:
        raise ValueError("a point has 3 numbers: x, y, z")
    if radius < 0:
        raise ValueError("radius cannot be negative")
    dx, dy, dz = point[0] - centre[0], point[1] - centre[1], point[2] - centre[2]
    return 1 if dx * dx + dy * dy + dz * dz <= radius * radius else 0
