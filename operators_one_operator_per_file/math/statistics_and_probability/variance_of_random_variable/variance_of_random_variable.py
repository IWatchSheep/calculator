"""Variance of random variable   [Var(X)]

Category : Math > Statistics and probability
Formula  : Var(X) = E[X²] − (E[X])²

Status   : ready to use - call compute(values, probs)
"""

NAME = 'Variance of random variable'
SYMBOL = 'Var(X)'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'Var(X) = E[X²] − (E[X])²'


def compute(values, probs):
    """Var(X) = E[X²] − (E[X])²"""
    return sum(x * x * p for x, p in zip(values, probs)) - sum(x * p for x, p in zip(values, probs)) ** 2
