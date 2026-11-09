"""Limit superior   [lim sup]

Category : Math > Real analysis
Formula  : lim sup aₙ = lim_{n→∞} sup{ aₖ : k ≥ n }

Status   : ready to use - call compute(terms)
"""

NAME = 'Limit superior'
SYMBOL = 'lim sup'
CATEGORY = 'Math'
SUBCATEGORY = 'Real analysis'
FORMULA = 'lim sup aₙ = lim_{n→∞} sup{ aₖ : k ≥ n }'
import math
from operators_one_operator_per_file import _helpers as H


def compute(terms):
    """lim sup aₙ, estimated as the largest term in the second half of the list"""
    return max(terms[len(terms) // 2:])
