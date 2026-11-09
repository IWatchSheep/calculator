"""Capacitance   [Q = CV]

Category : Physics > Physics
Formula  : Q = C V

Status   : ready to use - call compute(C, V)
"""

NAME = 'Capacitance'
SYMBOL = 'Q = CV'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'Q = C V'


def compute(C, V):
    """Q = C V"""
    return C * V
