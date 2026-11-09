"""Limit inferior   [lim inf]

Category : Math > Real analysis
Formula  : lim inf aₙ = lim_{n→∞} inf{ aₖ : k ≥ n }

Status   : ready to use - call compute(terms)
"""

NAME = 'Limit inferior'
SYMBOL = 'lim inf'
CATEGORY = 'Math'
SUBCATEGORY = 'Real analysis'
FORMULA = 'lim inf aₙ = lim_{n→∞} inf{ aₖ : k ≥ n }'
import math
from operators_one_operator_per_file import _helpers as H


def compute(terms):
    """lim inf aₙ, estimated as the smallest term in the second half of the list"""
    return min(terms[len(terms) // 2:])
