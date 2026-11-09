"""Final velocity   [v = u + at]

Category : Physics > Physics
Formula  : v = u + a t

Status   : ready to use - call compute(u, a, t)
"""

NAME = 'Final velocity'
SYMBOL = 'v = u + at'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'v = u + a t'


def compute(u, a, t):
    """v = u + a t"""
    return u + a * t
