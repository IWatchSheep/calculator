"""Time to a distance   [s = ut + ½at²]

Category : Physics > Physics
Formula  : the smallest t ≥ 0 with s = u t + ½ a t²   (s is the signed displacement)

Status   : ready to use - call compute(u, a, s)
"""
import math

NAME = 'Time to a distance'
SYMBOL = 's = ut + ½at²'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'the smallest t ≥ 0 with s = u t + ½ a t²   (s is the signed displacement)'


def compute(u, a, s):
    """the smallest t ≥ 0 that covers the signed displacement s"""
    if a == 0:
        if u == 0:
            if s == 0:
                return 0.0
            raise ValueError("not moving")
        t = s / u
        if t < 0:
            raise ValueError("that distance is not reached")
        return t + 0.0
    disc = u * u + 2 * a * s
    if disc < 0:
        raise ValueError("that distance is not reached")
    root = math.sqrt(disc)
    times = [t for t in ((-u + root) / a, (-u - root) / a) if t >= 0]
    if not times:
        raise ValueError("that distance is not reached")
    return min(times) + 0.0
