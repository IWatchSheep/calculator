"""Potential energy   [mgh]

Category : Physics > Physics
Formula  : PE = m g h

Status   : ready to use - call compute(m, h, g=9.81)
"""

NAME = 'Potential energy'
SYMBOL = 'mgh'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'PE = m g h'


def compute(m, h, g=9.81):
    """PE = m g h"""
    return m * g * h
