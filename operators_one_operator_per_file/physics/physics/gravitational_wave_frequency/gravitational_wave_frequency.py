"""Gravitational-wave frequency   [f_gw = 2 f_orb]

Category : Physics > Physics
Formula  : f_gw = 2 f_orb   (a circular binary radiates at twice its orbital frequency)

Status   : ready to use - call compute(f_orb)
"""
import math

NAME = 'Gravitational-wave frequency'
SYMBOL = 'f_gw = 2 f_orb'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'f_gw = 2 f_orb   (a circular binary radiates at twice its orbital frequency)'


def compute(f_orb):
    """f_gw = 2 f_orb, hertz"""
    if f_orb < 0:
        raise ValueError("a frequency cannot be negative")
    return 2 * f_orb
