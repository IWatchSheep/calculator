"""Stopping distance   [s = −u²/2a]

Category : Physics > Physics
Formula  : s = −u² / (2 a)   (the signed displacement until the speed is 0; a must oppose u)

Status   : ready to use - call compute(u, a)
"""
import math

NAME = 'Stopping distance'
SYMBOL = 's = −u²/2a'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 's = −u² / (2 a)   (the signed displacement until the speed is 0; a must oppose u)'


def compute(u, a):
    """the signed displacement until the speed is 0"""
    if u != 0 and a == 0:
        raise ValueError("no acceleration, it does not stop")
    if u * a > 0:
        raise ValueError("it is speeding up, it does not stop")
    if u == 0:
        return 0.0
    return -u * u / (2 * a)
