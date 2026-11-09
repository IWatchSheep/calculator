"""Isomorphism   [≅]

Category : Math > Abstract algebra
Formula  : A bijective homomorphism; G ≅ H means G and H have the same structure

Status   : ready to use - call compute(phi, G, H_, op1, op2)
"""

NAME = 'Isomorphism'
SYMBOL = '≅'
CATEGORY = 'Math'
SUBCATEGORY = 'Abstract algebra'
FORMULA = 'A bijective homomorphism; G ≅ H means G and H have the same structure'
import math
from operators_one_operator_per_file import _helpers as H


def compute(phi, G, H_, op1, op2):
    """True if φ is a bijection from G onto H that keeps the operation (φ(a∘b) = φ(a)∘φ(b))"""
    G, H_ = list(G), set(H_)
    images = [phi(g) for g in G]
    if len(set(images)) != len(G) or set(images) != H_:
        return False
    return all(phi(op1(a, b)) == op2(phi(a), phi(b)) for a in G for b in G)
