"""Natural log   [ln]

Category : Math > Algebra
Formula  : ln(x) = logₑ(x)

Status   : ready to use - call compute(x)
"""
import math

NAME = 'Natural log'
SYMBOL = 'ln'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = 'ln(x) = logₑ(x)'


def compute(x):
    """ln(x) = logₑ(x)"""
    return math.log(x)
