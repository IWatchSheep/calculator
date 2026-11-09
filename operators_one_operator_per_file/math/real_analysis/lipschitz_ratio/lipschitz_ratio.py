"""Lipschitz ratio   [K]

Category : Math > Real analysis
Formula  : |f(x) − f(y)| ≤ K |x − y|;  this returns |f(x) − f(y)| / |x − y|

Status   : ready to use - call compute(f, x, y)
"""

NAME = 'Lipschitz ratio'
SYMBOL = 'K'
CATEGORY = 'Math'
SUBCATEGORY = 'Real analysis'
FORMULA = '|f(x) − f(y)| ≤ K |x − y|;  this returns |f(x) − f(y)| / |x − y|'


def compute(f, x, y):
    """|f(x) − f(y)| ≤ K |x − y|;  this returns |f(x) − f(y)| / |x − y|"""
    return abs(f(x) - f(y)) / abs(x - y)
