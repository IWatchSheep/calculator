"""Uniform distribution   [U(a, b)]

Category : Math > Statistics and probability
Formula  : f(x) = 1 / (b − a) for a ≤ x ≤ b, else 0

Status   : ready to use - call compute(x, a, b)
"""

NAME = 'Uniform distribution'
SYMBOL = 'U(a, b)'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'f(x) = 1 / (b − a) for a ≤ x ≤ b, else 0'


def compute(x, a, b):
    """f(x) = 1 / (b − a) for a ≤ x ≤ b, else 0"""
    return 1 / (b - a) if a <= x <= b else 0
