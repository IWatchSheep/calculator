"""Acceleration   [a = Δv/t]

Category : Physics > Physics
Formula  : a = Δv / t

Status   : ready to use - call compute(delta_v, t)
"""

NAME = 'Acceleration'
SYMBOL = 'a = Δv/t'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'a = Δv / t'


def compute(delta_v, t):
    """a = Δv / t"""
    return delta_v / t
