"""Symmetric group order   [Sₙ]

Category : Math > Abstract algebra
Formula  : |Sₙ| = n!   (all permutations of n objects)

Status   : ready to use - call compute(n)
"""
import math

NAME = 'Symmetric group order'
SYMBOL = 'Sₙ'
CATEGORY = 'Math'
SUBCATEGORY = 'Abstract algebra'
FORMULA = '|Sₙ| = n!   (all permutations of n objects)'


def compute(n):
    """|Sₙ| = n!   (all permutations of n objects)"""
    return math.factorial(n)
