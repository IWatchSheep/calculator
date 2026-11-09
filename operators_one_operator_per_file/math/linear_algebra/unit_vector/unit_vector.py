"""Unit vector   [v̂]

Category : Math > Linear algebra
Formula  : v̂ = v / ‖v‖

Status   : ready to use - call compute(v)
"""
import math

NAME = 'Unit vector'
SYMBOL = 'v̂'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'v̂ = v / ‖v‖'


def compute(v):
    """v̂ = v / ‖v‖"""
    return [x / math.hypot(*v) for x in v]
