"""Tangent   [tan]

Category : Math > Trigonometry
Formula  : tan θ = sin θ / cos θ

Status   : ready to use - call compute(theta)
"""
import math

NAME = 'Tangent'
SYMBOL = 'tan'
CATEGORY = 'Math'
SUBCATEGORY = 'Trigonometry'
FORMULA = 'tan θ = sin θ / cos θ'


def compute(theta):
    """tan θ = sin θ / cos θ"""
    return math.tan(theta)
