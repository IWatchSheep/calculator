"""Least common multiple   [lcm]

Category : Math > Discrete and number theory
Formula  : lcm(a, b) = |a·b| / gcd(a, b)

Status   : ready to use - call compute(a, b)
"""
import math

NAME = 'Least common multiple'
SYMBOL = 'lcm'
CATEGORY = 'Math'
SUBCATEGORY = 'Discrete and number theory'
FORMULA = 'lcm(a, b) = |a·b| / gcd(a, b)'


def compute(a, b):
    """lcm(a, b) = |a·b| / gcd(a, b)"""
    return math.lcm(a, b)
