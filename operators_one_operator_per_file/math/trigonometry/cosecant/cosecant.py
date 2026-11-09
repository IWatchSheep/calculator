"""Cosecant   [csc]

Category : Math > Trigonometry
Formula  : csc θ = 1 / sin θ

Status   : ready to use - call compute(theta)
"""
import math

NAME = 'Cosecant'
SYMBOL = 'csc'
CATEGORY = 'Math'
SUBCATEGORY = 'Trigonometry'
FORMULA = 'csc θ = 1 / sin θ'


def compute(theta):
    """csc θ = 1 / sin θ"""
    return 1 / math.sin(theta)
