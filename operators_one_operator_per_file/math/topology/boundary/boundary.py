"""Boundary   [∂A]

Category : Math > Topology
Formula  : ∂A = Ā − A°

Status   : ready to use - call compute(tau, A)
"""

NAME = 'Boundary'
SYMBOL = '∂A'
CATEGORY = 'Math'
SUBCATEGORY = 'Topology'
FORMULA = '∂A = Ā − A°'
import math
from operators_one_operator_per_file import _helpers as H


def _space(tau):
    return frozenset().union(*[frozenset(u) for u in tau]) if tau else frozenset()


def _opens(tau):
    return [frozenset(u) for u in tau]


def compute(tau, A):
    """∂A = closure(A) − interior(A)"""
    X, A = _space(tau), frozenset(A)
    out = X
    for u in _opens(tau):
        if A <= X - u:
            out = out & (X - u)
    inner = frozenset()
    for u in _opens(tau):
        if u <= A:
            inner |= u
    return out - inner
