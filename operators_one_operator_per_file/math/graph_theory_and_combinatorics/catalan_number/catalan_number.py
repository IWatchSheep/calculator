"""Catalan number   [Cₙ]

Category : Math > Graph theory and combinatorics
Formula  : Cₙ = C(2n, n) / (n + 1)

Status   : ready to use - call compute(n)
"""
import math

NAME = 'Catalan number'
SYMBOL = 'Cₙ'
CATEGORY = 'Math'
SUBCATEGORY = 'Graph theory and combinatorics'
FORMULA = 'Cₙ = C(2n, n) / (n + 1)'


def compute(n):
    """Cₙ = C(2n, n) / (n + 1)"""
    return math.comb(2 * n, n) // (n + 1)
