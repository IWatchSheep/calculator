"""Hyperbolic tangent   [tanh]

Category : Math > Trigonometry
Formula  : tanh x = sinh x / cosh x

Status   : ready to use - call compute(x)
"""
import math

NAME = 'Hyperbolic tangent'
SYMBOL = 'tanh'
CATEGORY = 'Math'
SUBCATEGORY = 'Trigonometry'
FORMULA = 'tanh x = sinh x / cosh x'


def compute(x):
    """tanh x = sinh x / cosh x"""
    return math.tanh(x)
