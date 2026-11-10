"""Projectile time of flight   [T = 2v sin θ / g]

Category : Physics > Physics
Formula  : T = 2 v sin θ / g   (back to the same height, no drag, g = 9.81 m/s², θ in radians)

Status   : ready to use - call compute(v, angle, g=9.81)
"""
import math

NAME = 'Projectile time of flight'
SYMBOL = 'T = 2v sin θ / g'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'T = 2 v sin θ / g   (back to the same height, no drag, g = 9.81 m/s², θ in radians)'


def compute(v, angle, g=9.81):
    """T = 2 v sin θ / g"""
    if v < 0:
        raise ValueError("speed cannot be negative")
    if abs(angle) > math.pi / 2:
        raise ValueError("the angle is past straight up")
    if g <= 0:
        raise ValueError("gravity must pull downward")
    return 2 * v * math.sin(angle) / g
