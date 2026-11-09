"""Round up   [ceil]

Category : Math > Arithmetic
Formula  : ⌈x⌉ = smallest integer ≥ x

Status   : ready to use - call compute(x)
"""
import math

NAME = 'Round up'
SYMBOL = 'ceil'
CATEGORY = 'Math'
SUBCATEGORY = 'Arithmetic'
FORMULA = '⌈x⌉ = smallest integer ≥ x'


def compute(x):
    """⌈x⌉ = smallest integer ≥ x"""
    return math.ceil(x)
