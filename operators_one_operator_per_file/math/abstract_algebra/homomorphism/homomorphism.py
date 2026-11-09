"""Homomorphism   [φ: G → H]

Category : Math > Abstract algebra
Formula  : A map with φ(a∘b) = φ(a)∘φ(b)

Status   : ready to use - call compute(phi, G, op1, op2)
"""

NAME = 'Homomorphism'
SYMBOL = 'φ: G → H'
CATEGORY = 'Math'
SUBCATEGORY = 'Abstract algebra'
FORMULA = 'A map with φ(a∘b) = φ(a)∘φ(b)'
import math
from operators_one_operator_per_file import _helpers as H


def compute(phi, G, op1, op2):
    """True if φ(a∘b) = φ(a)∘φ(b) for all a, b in G  (op1 acts in G, op2 on the images)"""
    G = list(G)
    return all(phi(op1(a, b)) == op2(phi(a), phi(b)) for a in G for b in G)
