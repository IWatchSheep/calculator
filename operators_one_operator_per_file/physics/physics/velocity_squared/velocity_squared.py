"""Velocity squared   [v² = u² + 2as]

Category : Physics > Physics
Formula  : v = √(u² + 2 a s)

Status   : ready to use - call compute(u, a, s)
"""
import math

NAME = 'Velocity squared'
SYMBOL = 'v² = u² + 2as'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'v = √(u² + 2 a s)'


def compute(u, a, s):
    """v = √(u² + 2 a s)"""
    return math.sqrt(u * u + 2 * a * s)
