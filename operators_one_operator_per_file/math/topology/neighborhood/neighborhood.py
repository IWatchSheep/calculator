"""Neighborhood   [N(x)]

Category : Math > Topology
Formula  : A set containing an open set that contains x

Status   : ready to use - call compute(tau, x, N)
"""

NAME = 'Neighborhood'
SYMBOL = 'N(x)'
CATEGORY = 'Math'
SUBCATEGORY = 'Topology'
FORMULA = 'A set containing an open set that contains x'
import math
from operators_one_operator_per_file import _helpers as H


def _space(tau):
    return frozenset().union(*[frozenset(u) for u in tau]) if tau else frozenset()


def _opens(tau):
    return [frozenset(u) for u in tau]


def compute(tau, x, N):
    """True if N is a neighbourhood of x: some open set U has x ∈ U ⊆ N"""
    N = frozenset(N)
    return any(x in u and u <= N for u in _opens(tau))
