"""Alternating group order   [Aₙ]

Category : Math > Abstract algebra
Formula  : |Aₙ| = n!/2   (even permutations, n ≥ 2)

Status   : ready to use - call compute(n)
"""
import math

NAME = 'Alternating group order'
SYMBOL = 'Aₙ'
CATEGORY = 'Math'
SUBCATEGORY = 'Abstract algebra'
FORMULA = '|Aₙ| = n!/2   (even permutations, n ≥ 2)'


def compute(n):
    """|Aₙ| = n!/2   (even permutations, n ≥ 2)"""
    return math.factorial(n) // 2
