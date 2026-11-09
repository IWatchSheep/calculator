"""Dirac delta   [δ(x)]

Category : Math > Transforms and differential equations
Formula  : δ(x) = 0 for x ≠ 0 and ∫ δ(x) dx = 1

Status   : ready to use - call compute(x)
"""

NAME = 'Dirac delta'
SYMBOL = 'δ(x)'
CATEGORY = 'Math'
SUBCATEGORY = 'Transforms and differential equations'
FORMULA = 'δ(x) = 0 for x ≠ 0 and ∫ δ(x) dx = 1'
import math
from operators_one_operator_per_file import _helpers as H


def compute(x):
    """δ(x): 0 everywhere except at 0, where it is infinitely tall"""
    return math.inf if x == 0 else 0
