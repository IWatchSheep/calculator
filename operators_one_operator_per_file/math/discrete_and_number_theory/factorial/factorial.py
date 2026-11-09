"""Factorial   [n!]

Category : Math > Discrete and number theory
Formula  : n! = n · (n−1) · … · 2 · 1

Status   : ready to use - call compute(n)
"""
import math

NAME = 'Factorial'
SYMBOL = 'n!'
CATEGORY = 'Math'
SUBCATEGORY = 'Discrete and number theory'
FORMULA = 'n! = n · (n−1) · … · 2 · 1'


def compute(n):
    """n! = n · (n−1) · … · 2 · 1"""
    return math.factorial(n)
