"""Schwarzschild g_tt   [g_tt = −(1 − Rs/r)]

Category : Physics > Physics
Formula  : g_tt = −(1 − Rs/r)   (the time coefficient of the Schwarzschild metric outside a spherical mass, signature (−, +, +, +); r and Rs in metres)

Status   : ready to use - call compute(r, Rs)
"""
import math

NAME = 'Schwarzschild g_tt'
SYMBOL = 'g_tt = −(1 − Rs/r)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'g_tt = −(1 − Rs/r)   (the time coefficient of the Schwarzschild metric outside a spherical mass, signature (−, +, +, +); r and Rs in metres)'


def compute(r, Rs):
    """g_tt = −(1 − Rs/r)"""
    if r <= 0:
        raise ValueError("a radius must be positive")
    if Rs < 0:
        raise ValueError("the horizon radius cannot be negative")
    if r <= Rs:
        raise ValueError("r is not outside the horizon")
    return -(1 - Rs / r)
