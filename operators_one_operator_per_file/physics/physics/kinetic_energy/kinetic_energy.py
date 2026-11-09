"""Kinetic energy   [½mv²]

Category : Physics > Physics
Formula  : KE = ½ m v²

Status   : ready to use - call compute(m, v)
"""

NAME = 'Kinetic energy'
SYMBOL = '½mv²'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'KE = ½ m v²'


def compute(m, v):
    """KE = ½ m v²"""
    return 0.5 * m * v ** 2
