"""Kalman update variance   [p⁺ = (1 − k)p]

Category : Physics > Physics
Formula  : k = p / (p + r),  p⁺ = (1 − k) p   (kept out of the three-row step: the robot needs this variance for the next step)

Status   : ready to use - call compute(p, r)
"""
import math

NAME = 'Kalman update variance'
SYMBOL = 'p⁺ = (1 − k)p'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'k = p / (p + r),  p⁺ = (1 − k) p   (kept out of the three-row step: the robot needs this variance for the next step)'


def compute(p, r):
    """p⁺ = (1 − k) p with the gain k = p / (p + r)"""
    if p < 0:
        raise ValueError("a variance cannot be negative")
    if r <= 0:
        raise ValueError("measurement noise must be positive")
    k = p / (p + r)
    return (1 - k) * p
