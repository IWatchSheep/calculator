"""Basis   [{e₁, …, eₙ}]

Category : Math > Abstract algebra
Formula  : A linearly independent set that spans the vector space

Status   : ready to use - call compute(vectors)
"""

NAME = 'Basis'
SYMBOL = '{e₁, …, eₙ}'
CATEGORY = 'Math'
SUBCATEGORY = 'Abstract algebra'
FORMULA = 'A linearly independent set that spans the vector space'
import math
from operators_one_operator_per_file import _helpers as H


def compute(vectors):
    """A basis chosen from the given vectors (the rows): the independent ones"""
    pivots = H.rref(H.transpose(vectors))[1]
    return [list(vectors[i]) for i in pivots]
