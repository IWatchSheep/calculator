"""Kerr g_tφ   [g_tφ = −Rs a / r]

Category : Physics > Physics
Formula  : g_tφ = −Rs a / r   (the equator value of the frame-dragging coefficient of the Kerr metric; a = J/(M c) in metres; positive a gives a negative answer)

Status   : ready to use - call compute(r, Rs, a)
"""
import math

NAME = 'Kerr g_tφ'
SYMBOL = 'g_tφ = −Rs a / r'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'g_tφ = −Rs a / r   (the equator value of the frame-dragging coefficient of the Kerr metric; a = J/(M c) in metres; positive a gives a negative answer)'


def compute(r, Rs, a):
    """g_tφ = −Rs a / r on the equator"""
    if r <= 0:
        raise ValueError("a radius must be positive")
    if Rs <= 0:
        raise ValueError("the horizon radius must be positive")
    if abs(a) > Rs / 2:
        raise ValueError("the spin is past the extreme Kerr limit")
    return -Rs * a / r + 0.0
