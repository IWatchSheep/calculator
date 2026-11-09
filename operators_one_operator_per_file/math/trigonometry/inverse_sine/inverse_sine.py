"""Inverse sine   [asin]

Category : Math > Trigonometry
Formula  : θ = arcsin(x),  −1 ≤ x ≤ 1

Status   : ready to use - call compute(x)
"""
import math

NAME = 'Inverse sine'
SYMBOL = 'asin'
CATEGORY = 'Math'
SUBCATEGORY = 'Trigonometry'
FORMULA = 'θ = arcsin(x),  −1 ≤ x ≤ 1'


def compute(x):
    """θ = arcsin(x),  −1 ≤ x ≤ 1"""
    return math.asin(x)
