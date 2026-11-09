"""Subgroup   [H ≤ G]

Category : Math > Abstract algebra
Formula  : A subset H of G that is itself a group under the same operation

Status   : ready to use - call compute(H_, G, op)
"""

NAME = 'Subgroup'
SYMBOL = 'H ≤ G'
CATEGORY = 'Math'
SUBCATEGORY = 'Abstract algebra'
FORMULA = 'A subset H of G that is itself a group under the same operation'
import math
from operators_one_operator_per_file import _helpers as H


def compute(H_, G, op):
    """True if H is a subgroup of G: inside G, closed, contains the identity, and has inverses"""
    H_, G = list(H_), list(G)
    if not H_ or any(h not in G for h in H_):
        return False
    if any(op(a, b) not in H_ for a in H_ for b in H_):
        return False
    ids = [e for e in G if all(op(e, a) == a and op(a, e) == a for a in G)]
    if not ids or ids[0] not in H_:
        return False
    return all(any(op(a, b) == ids[0] for b in H_) for a in H_)
