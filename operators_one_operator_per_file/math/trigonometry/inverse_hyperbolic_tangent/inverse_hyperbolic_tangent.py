"""Inverse hyperbolic tangent   [atanh]

Category : Math > Trigonometry
Formula  : atanh x = ½ ln((1 + x)/(1 − x)),  |x| < 1

Status   : ready to use - call compute(x)
"""
import math

NAME = 'Inverse hyperbolic tangent'
SYMBOL = 'atanh'
CATEGORY = 'Math'
SUBCATEGORY = 'Trigonometry'
FORMULA = 'atanh x = ½ ln((1 + x)/(1 − x)),  |x| < 1'


def compute(x):
    """atanh x = ½ ln((1 + x)/(1 − x)),  |x| < 1"""
    return math.atanh(x)
