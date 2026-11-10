"""Projectile range   [R = v² sin 2θ / g]

Category : Physics > Physics
Formula  : R = v² sin(2θ) / g   (level ground, no drag, g = 9.81 m/s², θ in radians)

Status   : ready to use - call compute(v, angle, g=9.81)
"""
import math

NAME = 'Projectile range'
SYMBOL = 'R = v² sin 2θ / g'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'R = v² sin(2θ) / g   (level ground, no drag, g = 9.81 m/s², θ in radians)'


def compute(v, angle, g=9.81):
    """R = v² sin 2θ / g"""
    if v < 0:
        raise ValueError("speed cannot be negative")
    if abs(angle) > math.pi / 2:
        raise ValueError("the angle is past straight up")
    if g <= 0:
        raise ValueError("gravity must pull downward")
    return v * v * math.sin(2 * angle) / g
