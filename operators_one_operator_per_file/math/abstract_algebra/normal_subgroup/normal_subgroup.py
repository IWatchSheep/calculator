"""Normal subgroup   [N ◁ G]

Category : Math > Abstract algebra
Formula  : A subgroup N with gNg⁻¹ = N for every g in G

Status   : ready to use - call compute(N, G, op)
"""

NAME = 'Normal subgroup'
SYMBOL = 'N ◁ G'
CATEGORY = 'Math'
SUBCATEGORY = 'Abstract algebra'
FORMULA = 'A subgroup N with gNg⁻¹ = N for every g in G'
import math
from operators_one_operator_per_file import _helpers as H


def compute(N, G, op):
    """True if N is a subgroup of G and g·n·g⁻¹ stays in N for every g in G and n in N"""
    N, G = list(N), list(G)
    ids = [e for e in G if all(op(e, a) == a and op(a, e) == a for a in G)]
    if not ids or ids[0] not in N or any(op(a, b) not in N for a in N for b in N):
        return False
    inv = lambda g: next(h for h in G if op(g, h) == ids[0])
    return all(op(op(g, n), inv(g)) in N for g in G for n in N)
