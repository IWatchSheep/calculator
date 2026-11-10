"""Point inside a tree trunk   [a vertical cylinder]

Category : Physics > Physics
Formula  : 1 if the point is inside or on the vertical cylinder standing on z = 0 at (cx, cy), out to radius R and up to height h; 0 otherwise

Status   : ready to use - call compute(centre, radius, height, point)
"""
import math

NAME = 'Point inside a tree trunk'
SYMBOL = 'a vertical cylinder'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = '1 if the point is inside or on the vertical cylinder standing on z = 0 at (cx, cy), out to radius R and up to height h; 0 otherwise'


def compute(centre, radius, height, point):
    """1 if the point is inside or on the tree trunk, 0 if outside"""
    if len(centre) != 2:
        raise ValueError("a centre has 2 numbers: x, y")
    if len(point) != 3:
        raise ValueError("a point has 3 numbers: x, y, z")
    if radius < 0:
        raise ValueError("radius cannot be negative")
    if height < 0:
        raise ValueError("a length cannot be negative")
    dx, dy = point[0] - centre[0], point[1] - centre[1]
    return 1 if dx * dx + dy * dy <= radius * radius and 0 <= point[2] <= height else 0
