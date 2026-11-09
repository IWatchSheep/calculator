"""Inverse cosine   [acos]

Category : Math > Trigonometry
Formula  : θ = arccos(x),  −1 ≤ x ≤ 1

Status   : ready to use - call compute(x)
"""
import math

NAME = 'Inverse cosine'
SYMBOL = 'acos'
CATEGORY = 'Math'
SUBCATEGORY = 'Trigonometry'
FORMULA = 'θ = arccos(x),  −1 ≤ x ≤ 1'


def compute(x):
    """θ = arccos(x),  −1 ≤ x ≤ 1"""
    return math.acos(x)
