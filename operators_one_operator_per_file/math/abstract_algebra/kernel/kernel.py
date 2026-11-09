"""Kernel   [ker φ]

Category : Math > Abstract algebra
Formula  : ker φ = { g ∈ G : φ(g) = e_H }

Status   : ready to use - call compute(phi, G, identity)
"""

NAME = 'Kernel'
SYMBOL = 'ker φ'
CATEGORY = 'Math'
SUBCATEGORY = 'Abstract algebra'
FORMULA = 'ker φ = { g ∈ G : φ(g) = e_H }'
import math
from operators_one_operator_per_file import _helpers as H


def compute(phi, G, identity):
    """ker φ = { g ∈ G : φ(g) = identity of the target }"""
    return {g for g in G if phi(g) == identity}
