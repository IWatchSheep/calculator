"""Permutations   [nPr]

Category : Math > Discrete and number theory
Formula  : P(n, r) = n! / (n − r)!

Status   : ready to use - call compute(n, r)
"""
import math

NAME = 'Permutations'
SYMBOL = 'nPr'
CATEGORY = 'Math'
SUBCATEGORY = 'Discrete and number theory'
FORMULA = 'P(n, r) = n! / (n − r)!'


def compute(n, r):
    """P(n, r) = n! / (n − r)!"""
    return math.perm(n, r)
