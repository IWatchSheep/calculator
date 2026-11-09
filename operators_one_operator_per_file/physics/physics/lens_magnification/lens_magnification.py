"""Lens magnification   [m = −dᵢ/dₒ]

Category : Physics > Physics
Formula  : m = −dᵢ / dₒ   (negative m means an inverted image)

Status   : ready to use - call compute(d_i, d_o)
"""
import math

NAME = 'Lens magnification'
SYMBOL = 'm = −dᵢ/dₒ'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'm = −dᵢ / dₒ   (negative m means an inverted image)'


def compute(d_i, d_o):
    """m = −dᵢ / dₒ   (negative m means an inverted image)"""
    return -d_i / d_o
