"""Connected   [connected]

Category : Math > Topology
Formula  : Cannot be split into two disjoint non-empty open sets

Status   : ready to use - call compute(tau)
"""

NAME = 'Connected'
SYMBOL = 'connected'
CATEGORY = 'Math'
SUBCATEGORY = 'Topology'
FORMULA = 'Cannot be split into two disjoint non-empty open sets'
import math
from operators_one_operator_per_file import _helpers as H


def _space(tau):
    return frozenset().union(*[frozenset(u) for u in tau]) if tau else frozenset()


def _opens(tau):
    return [frozenset(u) for u in tau]


def compute(tau):
    """True if the space can't be split into two disjoint non-empty open sets"""
    X = _space(tau)
    opens = [u for u in _opens(tau) if u and u != X]
    return not any((u | v) == X and not (u & v) for u in opens for v in opens)
