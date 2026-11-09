"""Closed set   [F]

Category : Math > Topology
Formula  : A set whose complement is open

Status   : ready to use - call compute(tau, A)
"""

NAME = 'Closed set'
SYMBOL = 'F'
CATEGORY = 'Math'
SUBCATEGORY = 'Topology'
FORMULA = 'A set whose complement is open'
import math
from operators_one_operator_per_file import _helpers as H


def _space(tau):
    return frozenset().union(*[frozenset(u) for u in tau]) if tau else frozenset()


def _opens(tau):
    return [frozenset(u) for u in tau]


def compute(tau, A):
    """True if A is closed: its complement is open"""
    return (_space(tau) - frozenset(A)) in _opens(tau)
