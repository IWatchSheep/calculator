"""Open set   [U]

Category : Math > Topology
Formula  : A set U in a topology τ  (a member of τ)

Status   : ready to use - call compute(tau, U)
"""

NAME = 'Open set'
SYMBOL = 'U'
CATEGORY = 'Math'
SUBCATEGORY = 'Topology'
FORMULA = 'A set U in a topology τ  (a member of τ)'
import math
from operators_one_operator_per_file import _helpers as H


def _space(tau):
    return frozenset().union(*[frozenset(u) for u in tau]) if tau else frozenset()


def _opens(tau):
    return [frozenset(u) for u in tau]


def compute(tau, U):
    """True if U is one of the open sets of the topology tau"""
    return frozenset(U) in _opens(tau)
