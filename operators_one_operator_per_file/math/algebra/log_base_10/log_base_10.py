"""Log base 10   [log]

Category : Math > Algebra
Formula  : log₁₀(x)

Status   : ready to use - call compute(x)
"""
import math

NAME = 'Log base 10'
SYMBOL = 'log'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = 'log₁₀(x)'


def compute(x):
    """log₁₀(x)"""
    return math.log10(x)
