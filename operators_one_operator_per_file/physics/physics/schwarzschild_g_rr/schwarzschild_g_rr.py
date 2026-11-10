"""Schwarzschild g_rr   [g_rr = 1/(1 − Rs/r)]

Category : Physics > Physics
Formula  : g_rr = 1 / (1 − Rs/r)   (the radial coefficient of the Schwarzschild metric outside a spherical mass; r and Rs in metres)

Status   : ready to use - call compute(r, Rs)
"""
import math

NAME = 'Schwarzschild g_rr'
SYMBOL = 'g_rr = 1/(1 − Rs/r)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'g_rr = 1 / (1 − Rs/r)   (the radial coefficient of the Schwarzschild metric outside a spherical mass; r and Rs in metres)'


def compute(r, Rs):
    """g_rr = 1 / (1 − Rs/r)"""
    if r <= 0:
        raise ValueError("a radius must be positive")
    if Rs < 0:
        raise ValueError("the horizon radius cannot be negative")
    if r <= Rs:
        raise ValueError("r is not outside the horizon")
    return 1 / (1 - Rs / r)
