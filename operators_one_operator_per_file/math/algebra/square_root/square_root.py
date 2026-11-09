"""Square root   [√]

Category : Math > Algebra
Formula  : √x  (y such that y² = x)

Status   : ready to use - call compute(x)
"""
import math

NAME = 'Square root'
SYMBOL = '√'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = '√x  (y such that y² = x)'


def compute(x):
    """√x  (y such that y² = x)"""
    return math.sqrt(x)
