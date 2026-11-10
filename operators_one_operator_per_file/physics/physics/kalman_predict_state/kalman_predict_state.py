"""Kalman predict state   [x′ = x + ut]

Category : Physics > Physics
Formula  : x′ = x + u t   (the position a 1-D filter expects after coasting at speed u for time t)

Status   : ready to use - call compute(x, u, t)
"""
import math

NAME = 'Kalman predict state'
SYMBOL = 'x′ = x + ut'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'x′ = x + u t   (the position a 1-D filter expects after coasting at speed u for time t)'


def compute(x, u, t):
    """x′ = x + u t"""
    if t < 0:
        raise ValueError("time cannot be negative")
    return x + u * t
