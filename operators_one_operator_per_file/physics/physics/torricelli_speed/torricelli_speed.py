"""Torricelli's law   [v = √(2gh)]

Category : Physics > Physics
Formula  : v = √(2 g h)   (g = 9.81 m/s²)

Status   : ready to use - call compute(h, g)
"""
import math

NAME = "Torricelli's law"
SYMBOL = 'v = √(2gh)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'v = √(2 g h)   (g = 9.81 m/s²)'


def compute(h, g=9.81):
    """v = √(2 g h)   (g = 9.81 m/s²)"""
    return math.sqrt(2 * g * h)
