"""Basis of topology   [ℬ]

Category : Math > Topology
Formula  : A collection of open sets such that every open set is a union of members of ℬ

Status   : ready to use - call compute(tau, B)
"""

NAME = 'Basis of topology'
SYMBOL = 'ℬ'
CATEGORY = 'Math'
SUBCATEGORY = 'Topology'
FORMULA = 'A collection of open sets such that every open set is a union of members of ℬ'
import math
from operators_one_operator_per_file import _helpers as H


def _space(tau):
    return frozenset().union(*[frozenset(u) for u in tau]) if tau else frozenset()


def _opens(tau):
    return [frozenset(u) for u in tau]


def compute(tau, B):
    """True if every open set of tau is a union of members of B (and B's members are open)"""
    opens, B = set(_opens(tau)), _opens(B)
    if not all(b in opens for b in B):
        return False
    for u in opens:
        union = frozenset()
        for b in B:
            if b <= u:
                union |= b
        if union != u:
            return False
    return True
