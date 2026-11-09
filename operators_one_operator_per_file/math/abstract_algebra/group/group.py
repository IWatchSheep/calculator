"""Group   [(G, ∘)]

Category : Math > Abstract algebra
Formula  : A set G with an operation ∘ that is closed, associative, has an identity e, and every element has an inverse

Status   : ready to use - call compute(G, op)
"""

NAME = 'Group'
SYMBOL = '(G, ∘)'
CATEGORY = 'Math'
SUBCATEGORY = 'Abstract algebra'
FORMULA = 'A set G with an operation ∘ that is closed, associative, has an identity e, and every element has an inverse'
import math
from operators_one_operator_per_file import _helpers as H


def compute(G, op):
    """True if G with the operation op is a group: closed, associative, has an identity and inverses"""
    G = list(G)
    if any(op(a, b) not in G for a in G for b in G):
        return False
    if any(op(op(a, b), c) != op(a, op(b, c)) for a in G for b in G for c in G):
        return False
    ids = [e for e in G if all(op(e, a) == a and op(a, e) == a for a in G)]
    if not ids:
        return False
    return all(any(op(a, b) == ids[0] for b in G) for a in G)
