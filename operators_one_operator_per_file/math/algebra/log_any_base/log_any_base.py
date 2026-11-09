"""Log any base   [logₐ]

Category : Math > Algebra
Formula  : logₐ(x) = ln(x) / ln(a)

Status   : ready to use - call compute(x, base)
"""
import math

NAME = 'Log any base'
SYMBOL = 'logₐ'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = 'logₐ(x) = ln(x) / ln(a)'


def compute(x, base):
    """logₐ(x) = ln(x) / ln(a)"""
    return math.log(x, base)
