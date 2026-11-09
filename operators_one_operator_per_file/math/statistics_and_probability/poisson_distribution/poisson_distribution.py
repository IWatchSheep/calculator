"""Poisson distribution   [Pois(λ)]

Category : Math > Statistics and probability
Formula  : P(X = k) = λᵏ · e^(−λ) / k!

Status   : ready to use - call compute(k, lam)
"""
import math

NAME = 'Poisson distribution'
SYMBOL = 'Pois(λ)'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'P(X = k) = λᵏ · e^(−λ) / k!'


def compute(k, lam):
    """P(X = k) = λᵏ · e^(−λ) / k!"""
    return lam ** k * math.exp(-lam) / math.factorial(k)
