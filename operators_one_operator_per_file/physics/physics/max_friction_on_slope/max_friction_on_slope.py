"""Most friction on a slope   [f = μ m g cos θ]

Category : Physics > Physics
Formula  : f = μ m g cos θ   (the largest static friction, μ times the normal force, g = 9.81 m/s², θ in radians)

Status   : ready to use - call compute(mu, m, angle, g=9.81)
"""
import math

NAME = 'Most friction on a slope'
SYMBOL = 'f = μ m g cos θ'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'f = μ m g cos θ   (the largest static friction, μ times the normal force, g = 9.81 m/s², θ in radians)'


def compute(mu, m, angle, g=9.81):
    """f = μ m g cos θ"""
    if mu < 0:
        raise ValueError("friction cannot be negative")
    if m <= 0:
        raise ValueError("mass must be positive")
    if not 0 <= angle <= math.pi / 2:
        raise ValueError("the slope is past vertical")
    if g <= 0:
        raise ValueError("gravity must pull downward")
    return mu * m * g * math.cos(angle)
