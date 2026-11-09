"""Cotangent   [cot]

Category : Math > Trigonometry
Formula  : cot θ = cos θ / sin θ

Status   : ready to use - call compute(theta)
"""
import math

NAME = 'Cotangent'
SYMBOL = 'cot'
CATEGORY = 'Math'
SUBCATEGORY = 'Trigonometry'
FORMULA = 'cot θ = cos θ / sin θ'


def compute(theta):
    """cot θ = cos θ / sin θ"""
    return 1 / math.tan(theta)
