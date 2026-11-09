"""Closure   [Ā]

Category : Math > Topology
Formula  : Smallest closed set containing A

Status   : ready to use - call compute(tau, A)
"""

NAME = 'Closure'
SYMBOL = 'Ā'
CATEGORY = 'Math'
SUBCATEGORY = 'Topology'
FORMULA = 'Smallest closed set containing A'
import math
from operators_one_operator_per_file import _helpers as H


def _space(tau):
    return frozenset().union(*[frozenset(u) for u in tau]) if tau else frozenset()


def _opens(tau):
    return [frozenset(u) for u in tau]


def compute(tau, A):
    """The smallest closed set containing A"""
    X, A = _space(tau), frozenset(A)
    closed = [X - u for u in _opens(tau)]
    out = X
    for c in closed:
        if A <= c:
            out = out & c
    return out
