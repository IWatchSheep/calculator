"""Combinations   [nCr]

Category : Math > Discrete and number theory
Formula  : C(n, r) = n! / (r! (n − r)!)

Status   : ready to use - call compute(n, r)
"""
import math

NAME = 'Combinations'
SYMBOL = 'nCr'
CATEGORY = 'Math'
SUBCATEGORY = 'Discrete and number theory'
FORMULA = 'C(n, r) = n! / (r! (n − r)!)'


def compute(n, r):
    """C(n, r) = n! / (r! (n − r)!)"""
    return math.comb(n, r)
