"""Saturation   [clamp]

Category : Physics > Physics
Formula  : clamp(value, low, high)   (the value limited to the low and high ends)

Status   : ready to use - call compute(value, low, high)
"""
import math

NAME = 'Saturation'
SYMBOL = 'clamp'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'clamp(value, low, high)   (the value limited to the low and high ends)'


def compute(value, low, high):
    """the value, limited to the low and high ends"""
    if low > high:
        raise ValueError("the low limit is above the high limit")
    return min(max(value, low), high)
