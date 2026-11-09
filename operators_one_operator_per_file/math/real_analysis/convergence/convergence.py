"""Convergence   [→]

Category : Math > Real analysis
Formula  : aₙ → L if for every ε > 0 there is N with |aₙ − L| < ε for all n > N

Status   : ready to use - call compute(terms, L, eps)
"""

NAME = 'Convergence'
SYMBOL = '→'
CATEGORY = 'Math'
SUBCATEGORY = 'Real analysis'
FORMULA = 'aₙ → L if for every ε > 0 there is N with |aₙ − L| < ε for all n > N'
import math
from operators_one_operator_per_file import _helpers as H


def compute(terms, L, eps):
    """The first index N (counting from 0) after which every given term is within eps of L"""
    last_bad = -1
    for n, t in enumerate(terms):
        if abs(t - L) >= eps:
            last_bad = n
    if last_bad == len(terms) - 1:
        raise ValueError("the last term is not within eps of L")
    return last_bad + 1
