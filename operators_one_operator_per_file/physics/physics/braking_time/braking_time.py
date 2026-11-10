"""Braking time   [t = −u/a]

Category : Physics > Physics
Formula  : t = −u / a   (the time until the speed is 0; a must oppose u)

Status   : ready to use - call compute(u, a)
"""
import math

NAME = 'Braking time'
SYMBOL = 't = −u/a'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 't = −u / a   (the time until the speed is 0; a must oppose u)'


def compute(u, a):
    """the time until the speed is 0"""
    if u != 0 and a == 0:
        raise ValueError("no acceleration, it does not stop")
    if u * a > 0:
        raise ValueError("it is speeding up, it does not stop")
    if u == 0:
        return 0.0
    return -u / a
