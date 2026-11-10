"""Force down a slope   [F = mg sin θ]

Category : Physics > Physics
Formula  : F = m g sin θ   (the part of the weight that pulls down the slope, g = 9.81 m/s², θ in radians above the horizontal)

Status   : ready to use - call compute(m, angle, g=9.81)
"""
import math

NAME = 'Force down a slope'
SYMBOL = 'F = mg sin θ'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'F = m g sin θ   (the part of the weight that pulls down the slope, g = 9.81 m/s², θ in radians above the horizontal)'


def compute(m, angle, g=9.81):
    """F = m g sin θ"""
    if m <= 0:
        raise ValueError("mass must be positive")
    if not 0 <= angle <= math.pi / 2:
        raise ValueError("the slope is past vertical")
    if g <= 0:
        raise ValueError("gravity must pull downward")
    return m * g * math.sin(angle)
