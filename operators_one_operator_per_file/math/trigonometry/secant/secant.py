"""Secant   [sec]

Category : Math > Trigonometry
Formula  : sec θ = 1 / cos θ

Status   : ready to use - call compute(theta)
"""
import math

NAME = 'Secant'
SYMBOL = 'sec'
CATEGORY = 'Math'
SUBCATEGORY = 'Trigonometry'
FORMULA = 'sec θ = 1 / cos θ'


def compute(theta):
    """sec θ = 1 / cos θ"""
    return 1 / math.cos(theta)
