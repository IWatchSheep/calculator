"""Centripetal acceleration   [a = v²/r]

Category : Physics > Physics
Formula  : a = v² / r

Status   : ready to use - call compute(v, r)
"""

NAME = 'Centripetal acceleration'
SYMBOL = 'a = v²/r'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'a = v² / r'


def compute(v, r):
    """a = v² / r"""
    return v ** 2 / r
