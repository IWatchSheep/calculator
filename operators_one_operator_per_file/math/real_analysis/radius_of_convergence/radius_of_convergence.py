"""Radius of convergence   [R]

Category : Math > Real analysis
Formula  : R = 1 / L  where L = lim |aₙ₊₁ / aₙ|

Status   : ready to use - call compute(L)
"""
import math

NAME = 'Radius of convergence'
SYMBOL = 'R'
CATEGORY = 'Math'
SUBCATEGORY = 'Real analysis'
FORMULA = 'R = 1 / L  where L = lim |aₙ₊₁ / aₙ|'


def compute(L):
    """R = 1 / L  where L = lim |aₙ₊₁ / aₙ|"""
    return math.inf if L == 0 else 1 / L
