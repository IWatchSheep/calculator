"""Infinite-well probability density   [|ψ|² = (2/L) sin²(n π x / L)]

Category : Physics > Physics
Formula  : |ψ|² = (2/L) sin²(n π x / L)   (the probability per metre of finding a particle in a one-dimensional box at x; the walls are at 0 and L)

Status   : ready to use - call compute(n, L, x)
"""
import math

NAME = 'Infinite-well probability density'
SYMBOL = '|ψ|² = (2/L) sin²(n π x / L)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = '|ψ|² = (2/L) sin²(n π x / L)   (the probability per metre of finding a particle in a one-dimensional box at x; the walls are at 0 and L)'


def compute(n, L, x):
    """probability per metre"""
    if n < 1 or not float(n).is_integer():
        raise ValueError("a level must be a positive whole number")
    if L <= 0:
        raise ValueError("a length must be positive")
    if x < 0 or x > L:
        raise ValueError("the position is outside the box")
    return 2 / L * math.sin(n * math.pi * x / L) ** 2
