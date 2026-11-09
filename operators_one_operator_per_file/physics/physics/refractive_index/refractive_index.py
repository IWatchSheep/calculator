"""Refractive index   [n = c/v]

Category : Physics > Physics
Formula  : n = c / v   (c = 299 792 458 m/s)

Status   : ready to use - call compute(v, c)
"""
import math

NAME = 'Refractive index'
SYMBOL = 'n = c/v'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'n = c / v   (c = 299 792 458 m/s)'


def compute(v, c=299792458):
    """n = c / v   (c = 299 792 458 m/s)"""
    return c / v
