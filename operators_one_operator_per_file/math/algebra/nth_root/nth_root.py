"""Nth root   [ⁿ√]

Category : Math > Algebra
Formula  : ⁿ√x = x^(1/n)

Status   : ready to use - call compute(x, n)
"""

NAME = 'Nth root'
SYMBOL = 'ⁿ√'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = 'ⁿ√x = x^(1/n)'


def compute(x, n):
    """ⁿ√x = x^(1/n)"""
    return x ** (1 / n)
