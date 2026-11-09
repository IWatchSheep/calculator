"""Indefinite integral   [∫]

Category : Math > Calculus
Formula  : ∫ f(x) dx = F(x) + C   where F′(x) = f(x)

Status   : ready to use - call compute(f, x, C=0)
"""

NAME = 'Indefinite integral'
SYMBOL = '∫'
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = '∫ f(x) dx = F(x) + C   where F′(x) = f(x)'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, x, C=0):
    """∫ f(x) dx = F(x) + C, with F(x) = ∫ from 0 to x of f(t) dt  (numerical)"""
    return H.simpson(f, 0, x, 1000) + C
