"""Axiom of choice   [AC]

Category : Math > Category theory and foundations
Formula  : Every collection of non-empty sets has a choice function

Status   : ready to use - call compute(sets)
"""

NAME = 'Axiom of choice'
SYMBOL = 'AC'
CATEGORY = 'Math'
SUBCATEGORY = 'Category theory and foundations'
FORMULA = 'Every collection of non-empty sets has a choice function'
import math
from operators_one_operator_per_file import _helpers as H


def compute(sets):
    """A choice function for a finite list of non-empty sets: one element picked from each"""
    if any(len(s) == 0 for s in sets):
        raise ValueError("every set must be non-empty")
    return [sorted(s, key=str)[0] for s in sets]
