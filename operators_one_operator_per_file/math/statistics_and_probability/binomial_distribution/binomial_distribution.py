"""Binomial distribution   [B(n, p)]

Category : Math > Statistics and probability
Formula  : P(X = k) = C(n,k) · pᵏ · (1−p)ⁿ⁻ᵏ

Status   : ready to use - call compute(n, k, p)
"""
import math

NAME = 'Binomial distribution'
SYMBOL = 'B(n, p)'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'P(X = k) = C(n,k) · pᵏ · (1−p)ⁿ⁻ᵏ'


def compute(n, k, p):
    """P(X = k) = C(n,k) · pᵏ · (1−p)ⁿ⁻ᵏ"""
    return math.comb(n, k) * p ** k * (1 - p) ** (n - k)
