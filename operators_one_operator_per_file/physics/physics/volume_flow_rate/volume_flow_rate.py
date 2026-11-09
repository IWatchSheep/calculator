"""Volume flow rate   [Q = Av]

Category : Physics > Physics
Formula  : Q = A v

Status   : ready to use - call compute(A, v)
"""
import math

NAME = 'Volume flow rate'
SYMBOL = 'Q = Av'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'Q = A v'


def compute(A, v):
    """Q = A v"""
    return A * v
