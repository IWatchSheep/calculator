"""Image   [im φ]

Category : Math > Abstract algebra
Formula  : im φ = { φ(g) : g ∈ G }

Status   : ready to use - call compute(phi, G)
"""

NAME = 'Image'
SYMBOL = 'im φ'
CATEGORY = 'Math'
SUBCATEGORY = 'Abstract algebra'
FORMULA = 'im φ = { φ(g) : g ∈ G }'
import math
from operators_one_operator_per_file import _helpers as H


def compute(phi, G):
    """im φ = { φ(g) : g ∈ G }"""
    return {phi(g) for g in G}
