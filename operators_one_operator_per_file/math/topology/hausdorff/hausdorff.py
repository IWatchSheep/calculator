"""Hausdorff   [T₂]

Category : Math > Topology
Formula  : Any two distinct points have disjoint open neighborhoods

Status   : ready to use - call compute(tau)
"""

NAME = 'Hausdorff'
SYMBOL = 'T₂'
CATEGORY = 'Math'
SUBCATEGORY = 'Topology'
FORMULA = 'Any two distinct points have disjoint open neighborhoods'
import math
from operators_one_operator_per_file import _helpers as H


def _space(tau):
    return frozenset().union(*[frozenset(u) for u in tau]) if tau else frozenset()


def _opens(tau):
    return [frozenset(u) for u in tau]


def compute(tau):
    """True if any two different points have disjoint open neighbourhoods"""
    X, opens = sorted(_space(tau), key=str), _opens(tau)
    for i, p in enumerate(X):
        for q in X[i + 1:]:
            if not any(p in u and q in v and not (u & v) for u in opens for v in opens):
                return False
    return True
