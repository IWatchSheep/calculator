"""Pythagorean identity   [sin²θ+cos²θ=1]

Category : Math > Trigonometry
Formula  : sin²θ + cos²θ = 1  (function returns the left side, always 1)

Status   : ready to use - call compute(theta)
"""
import math

NAME = 'Pythagorean identity'
SYMBOL = 'sin²θ+cos²θ=1'
CATEGORY = 'Math'
SUBCATEGORY = 'Trigonometry'
FORMULA = 'sin²θ + cos²θ = 1  (function returns the left side, always 1)'


def compute(theta):
    """sin²θ + cos²θ = 1  (function returns the left side, always 1)"""
    return math.sin(theta) ** 2 + math.cos(theta) ** 2
