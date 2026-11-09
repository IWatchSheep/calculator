"""Hyperbolic cosine   [cosh]

Category : Math > Trigonometry
Formula  : cosh x = (eˣ + e⁻ˣ) / 2

Status   : ready to use - call compute(x)
"""
import math

NAME = 'Hyperbolic cosine'
SYMBOL = 'cosh'
CATEGORY = 'Math'
SUBCATEGORY = 'Trigonometry'
FORMULA = 'cosh x = (eˣ + e⁻ˣ) / 2'


def compute(x):
    """cosh x = (eˣ + e⁻ˣ) / 2"""
    return math.cosh(x)
