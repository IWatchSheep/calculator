"""Exponential distribution   [Exp(λ)]

Category : Math > Statistics and probability
Formula  : f(x) = λ · e^(−λx) for x ≥ 0

Status   : ready to use - call compute(x, lam)
"""
import math

NAME = 'Exponential distribution'
SYMBOL = 'Exp(λ)'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'f(x) = λ · e^(−λx) for x ≥ 0'


def compute(x, lam):
    """f(x) = λ · e^(−λx) for x ≥ 0"""
    return lam * math.exp(-lam * x) if x >= 0 else 0
