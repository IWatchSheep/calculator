"""Distance to a segment   [distance from a point to a segment]

Category : Physics > Physics
Formula  : t = ((p − a) · (b − a)) / |b − a|² clamped to 0..1;  the closest point is a + t (b − a);  the answer is the distance from p to it (metres)

Status   : ready to use - call compute(a, b, p)
"""
import math

NAME = 'Distance to a segment'
SYMBOL = 'distance from a point to a segment'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 't = ((p − a) · (b − a)) / |b − a|² clamped to 0..1;  the closest point is a + t (b − a);  the answer is the distance from p to it (metres)'


def compute(a, b, p):
    """the distance from the point p to the segment from a to b"""
    if len(a) != 3 or len(b) != 3 or len(p) != 3:
        raise ValueError("a point has 3 numbers: x, y, z")
    ab = [b[0] - a[0], b[1] - a[1], b[2] - a[2]]
    length2 = ab[0] * ab[0] + ab[1] * ab[1] + ab[2] * ab[2]
    if length2 == 0:
        raise ValueError("the segment has length zero")
    t = ((p[0] - a[0]) * ab[0] + (p[1] - a[1]) * ab[1] + (p[2] - a[2]) * ab[2]) / length2
    t = min(max(t, 0.0), 1.0)
    dx, dy, dz = p[0] - (a[0] + t * ab[0]), p[1] - (a[1] + t * ab[1]), p[2] - (a[2] + t * ab[2])
    return math.sqrt(dx * dx + dy * dy + dz * dz)
