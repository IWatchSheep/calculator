"""Laplace transform   [L{f}]

Category : Math > Transforms and differential equations
Formula  : F(s) = ∫₀^∞ f(t) e^(−st) dt

Status   : ready to use - call compute(f, s)
"""

NAME = 'Laplace transform'
SYMBOL = 'L{f}'
CATEGORY = 'Math'
SUBCATEGORY = 'Transforms and differential equations'
FORMULA = 'F(s) = ∫₀^∞ f(t) e^(−st) dt'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, s):
    """F(s) = ∫ from 0 to ∞ of f(t)·e^(−st) dt  (numerical, s > 0; type f with t)"""
    if s <= 0:
        raise ValueError("s must be positive")
    T = max(20.0, 40.0 / s)
    return H.simpson(lambda t: f(t) * math.exp(-s * t), 0, T, 20000)
