"""Kalman update   [x⁺ = x + k(z − x)]

Category : Physics > Physics
Formula  : k = p / (p + r),  x⁺ = x + k (z − x)   (the menu operator opens three rows: predict the state, predict the variance, then this update)

Status   : ready to use - call compute(x, p, z, r)
"""
import math

NAME = 'Kalman update'
SYMBOL = 'x⁺ = x + k(z − x)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'k = p / (p + r),  x⁺ = x + k (z − x)   (the menu operator opens three rows: predict the state, predict the variance, then this update)'


def compute(x, p, z, r):
    """x⁺ = x + k (z − x) with the gain k = p / (p + r)"""
    if p < 0:
        raise ValueError("a variance cannot be negative")
    if r <= 0:
        raise ValueError("measurement noise must be positive")
    k = p / (p + r)
    return x + k * (z - x)
