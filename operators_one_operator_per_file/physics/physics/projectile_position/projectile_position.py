"""Projectile position   [x, y at t]

Category : Physics > Physics
Formula  : x = v cos θ · t,  y = v sin θ · t − ½ g t²   (y is up, no drag, g = 9.81 m/s²)

Status   : ready to use - call compute(v, angle, t, g=9.81)
"""
import math

NAME = 'Projectile position'
SYMBOL = 'x, y at t'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'x = v cos θ · t,  y = v sin θ · t − ½ g t²   (y is up, no drag, g = 9.81 m/s²)'


def compute(v, angle, t, g=9.81):
    """[x, y] metres at time t after launch; y is up"""
    if v < 0:
        raise ValueError("speed cannot be negative")
    if abs(angle) > math.pi / 2:
        raise ValueError("the angle is past straight up")
    if g <= 0:
        raise ValueError("gravity must pull downward")
    if t < 0:
        raise ValueError("time cannot be negative")
    return [v * math.cos(angle) * t, v * math.sin(angle) * t - 0.5 * g * t * t]
