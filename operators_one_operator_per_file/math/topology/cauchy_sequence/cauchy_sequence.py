"""Cauchy sequence   [(xₙ)]

Category : Math > Topology
Formula  : For every ε > 0 there is N with d(xₘ, xₙ) < ε for all m, n > N

Status   : ready to use - call compute(terms, eps)
"""

NAME = 'Cauchy sequence'
SYMBOL = '(xₙ)'
CATEGORY = 'Math'
SUBCATEGORY = 'Topology'
FORMULA = 'For every ε > 0 there is N with d(xₘ, xₙ) < ε for all m, n > N'
import math
from operators_one_operator_per_file import _helpers as H


def compute(terms, eps):
    """The first index N after which every pair of the given terms is closer than eps (None if there isn't one)"""
    for N in range(len(terms)):
        tail = terms[N:]
        if max(tail) - min(tail) < eps:
            return N
    raise ValueError("the terms never settle within eps")
