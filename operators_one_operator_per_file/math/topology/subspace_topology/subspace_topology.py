"""Subspace topology   [τ_A]

Category : Math > Topology
Formula  : τ_A = { U ∩ A : U ∈ τ }

Status   : ready to use - call compute(tau, A)
"""

NAME = 'Subspace topology'
SYMBOL = 'τ_A'
CATEGORY = 'Math'
SUBCATEGORY = 'Topology'
FORMULA = 'τ_A = { U ∩ A : U ∈ τ }'
import math
from operators_one_operator_per_file import _helpers as H


def _space(tau):
    return frozenset().union(*[frozenset(u) for u in tau]) if tau else frozenset()


def _opens(tau):
    return [frozenset(u) for u in tau]


def compute(tau, A):
    """The open sets of the subspace A:  { U ∩ A : U open }"""
    A = frozenset(A)
    return {frozenset(u & A) for u in _opens(tau)}
