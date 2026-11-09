"""Interior   [A°]

Category : Math > Topology
Formula  : Largest open set contained in A

Status   : ready to use - call compute(tau, A)
"""

NAME = 'Interior'
SYMBOL = 'A°'
CATEGORY = 'Math'
SUBCATEGORY = 'Topology'
FORMULA = 'Largest open set contained in A'
import math
from operators_one_operator_per_file import _helpers as H


def _space(tau):
    return frozenset().union(*[frozenset(u) for u in tau]) if tau else frozenset()


def _opens(tau):
    return [frozenset(u) for u in tau]


def compute(tau, A):
    """The largest open set inside A"""
    A = frozenset(A)
    out = frozenset()
    for u in _opens(tau):
        if u <= A:
            out |= u
    return out
