"""Energy stored in an inductor   [U = ½LI²]

Category : Physics > Physics
Formula  : U = ½ L I²

Status   : ready to use - call compute(L, I)
"""
import math

NAME = 'Energy stored in an inductor'
SYMBOL = 'U = ½LI²'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'U = ½ L I²'


def compute(L, I):
    """U = ½ L I²"""
    return 0.5 * L * I ** 2
