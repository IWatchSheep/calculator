"""Displacement   [s = ut + ½at²]

Category : Physics > Physics
Formula  : s = u t + ½ a t²

Status   : ready to use - call compute(u, a, t)
"""

NAME = 'Displacement'
SYMBOL = 's = ut + ½at²'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 's = u t + ½ a t²'


def compute(u, a, t):
    """s = u t + ½ a t²"""
    return u * t + 0.5 * a * t ** 2
