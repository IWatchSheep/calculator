"""Kalman predict variance   [p′ = p + q]

Category : Physics > Physics
Formula  : p′ = p + q   (the uncertainty grows by the process noise q)

Status   : ready to use - call compute(p, q)
"""
import math

NAME = 'Kalman predict variance'
SYMBOL = 'p′ = p + q'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'p′ = p + q   (the uncertainty grows by the process noise q)'


def compute(p, q):
    """p′ = p + q"""
    if p < 0:
        raise ValueError("a variance cannot be negative")
    if q < 0:
        raise ValueError("process noise cannot be negative")
    return p + q
