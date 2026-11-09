"""Euler's number   [e]

Category : Math > Constants and relations
Formula  : e = lim (1 + 1/n)ⁿ ≈ 2.71828182…

Status   : ready to use - call compute()
"""
import math

NAME = "Euler's number"
SYMBOL = 'e'
CATEGORY = 'Math'
SUBCATEGORY = 'Constants and relations'
FORMULA = 'e = lim (1 + 1/n)ⁿ ≈ 2.71828182…'


def compute():
    """e = lim (1 + 1/n)ⁿ ≈ 2.71828182…"""
    return math.e
