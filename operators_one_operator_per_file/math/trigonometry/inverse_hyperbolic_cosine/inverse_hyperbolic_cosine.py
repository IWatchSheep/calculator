"""Inverse hyperbolic cosine   [acosh]

Category : Math > Trigonometry
Formula  : acosh x = ln(x + √(x² − 1)),  x ≥ 1

Status   : ready to use - call compute(x)
"""
import math

NAME = 'Inverse hyperbolic cosine'
SYMBOL = 'acosh'
CATEGORY = 'Math'
SUBCATEGORY = 'Trigonometry'
FORMULA = 'acosh x = ln(x + √(x² − 1)),  x ≥ 1'


def compute(x):
    """acosh x = ln(x + √(x² − 1)),  x ≥ 1"""
    return math.acosh(x)
