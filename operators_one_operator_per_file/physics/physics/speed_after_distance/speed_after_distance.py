"""Speed after a distance   [v² = u² + 2as]

Category : Physics > Physics
Formula  : v = √(u² + 2 a s)   (u in m/s, a in m/s², s in metres along the line)

Status   : ready to use - call compute(u, a, s)
"""
import math

NAME = 'Speed after a distance'
SYMBOL = 'v² = u² + 2as'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'v = √(u² + 2 a s)   (u in m/s, a in m/s², s in metres along the line)'


def compute(u, a, s):
    """v = √(u² + 2 a s), the speed (never negative) after s metres"""
    v2 = u * u + 2 * a * s
    if v2 < 0:
        raise ValueError("the motion stops before that distance")
    return math.sqrt(v2)
