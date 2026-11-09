"""Proportional to   [∝]

Category : Math > Constants and relations
Formula  : y ∝ x  means y = k·x;  returns the constant k = y / x

Status   : ready to use - call compute(x, y)
"""

NAME = 'Proportional to'
SYMBOL = '∝'
CATEGORY = 'Math'
SUBCATEGORY = 'Constants and relations'
FORMULA = 'y ∝ x  means y = k·x;  returns the constant k = y / x'


def compute(x, y):
    """y ∝ x  means y = k·x;  returns the constant k = y / x"""
    return y / x
