"""Tipping margin   [b cos θ − h sin θ]

Category : Physics > Physics
Formula  : b cos θ − h sin θ   (metres from the downhill foot to where the weight falls; positive stays upright)

Status   : ready to use - call compute(half_width, height, angle)
"""
import math

NAME = 'Tipping margin'
SYMBOL = 'b cos θ − h sin θ'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'b cos θ − h sin θ   (metres from the downhill foot to where the weight falls; positive stays upright)'


def compute(half_width, height, angle):
    """b cos θ − h sin θ"""
    if half_width < 0 or height < 0:
        raise ValueError("a length cannot be negative")
    if not 0 <= angle <= math.pi / 2:
        raise ValueError("the slope is past vertical")
    return half_width * math.cos(angle) - height * math.sin(angle)
