"""Hyperbolic sine   [sinh]

Category : Math > Trigonometry
Formula  : sinh x = (eˣ − e⁻ˣ) / 2

Status   : ready to use - call compute(x)
"""
import math

NAME = 'Hyperbolic sine'
SYMBOL = 'sinh'
CATEGORY = 'Math'
SUBCATEGORY = 'Trigonometry'
FORMULA = 'sinh x = (eˣ − e⁻ˣ) / 2'


def compute(x):
    """sinh x = (eˣ − e⁻ˣ) / 2"""
    return math.sinh(x)
