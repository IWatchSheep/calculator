"""Round down   [floor]

Category : Math > Arithmetic
Formula  : ⌊x⌋ = greatest integer ≤ x

Status   : ready to use - call compute(x)
"""
import math

NAME = 'Round down'
SYMBOL = 'floor'
CATEGORY = 'Math'
SUBCATEGORY = 'Arithmetic'
FORMULA = '⌊x⌋ = greatest integer ≤ x'


def compute(x):
    """⌊x⌋ = greatest integer ≤ x"""
    return math.floor(x)
