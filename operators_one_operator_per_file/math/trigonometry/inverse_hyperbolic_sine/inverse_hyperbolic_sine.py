"""Inverse hyperbolic sine   [asinh]

Category : Math > Trigonometry
Formula  : asinh x = ln(x + √(x² + 1))

Status   : ready to use - call compute(x)
"""
import math

NAME = 'Inverse hyperbolic sine'
SYMBOL = 'asinh'
CATEGORY = 'Math'
SUBCATEGORY = 'Trigonometry'
FORMULA = 'asinh x = ln(x + √(x² + 1))'


def compute(x):
    """asinh x = ln(x + √(x² + 1))"""
    return math.asinh(x)
