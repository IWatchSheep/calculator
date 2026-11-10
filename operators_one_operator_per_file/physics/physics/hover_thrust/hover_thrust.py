"""Hover thrust   [T = mg]

Category : Physics > Physics
Formula  : T = m g   (the upward force that balances the weight, g = 9.81 m/s²)

Status   : ready to use - call compute(m, g=9.81)
"""
import math

NAME = 'Hover thrust'
SYMBOL = 'T = mg'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'T = m g   (the upward force that balances the weight, g = 9.81 m/s²)'


def compute(m, g=9.81):
    """T = m g"""
    if m <= 0:
        raise ValueError("mass must be positive")
    if g <= 0:
        raise ValueError("gravity must pull downward")
    return m * g
