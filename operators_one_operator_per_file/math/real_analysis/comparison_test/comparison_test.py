"""Comparison test   [aₙ ≤ bₙ]

Category : Math > Real analysis
Formula  : If 0 ≤ aₙ ≤ bₙ and Σbₙ converges then Σaₙ converges

Status   : ready to use - call compute(a, b)
"""

NAME = 'Comparison test'
SYMBOL = 'aₙ ≤ bₙ'
CATEGORY = 'Math'
SUBCATEGORY = 'Real analysis'
FORMULA = 'If 0 ≤ aₙ ≤ bₙ and Σbₙ converges then Σaₙ converges'
import math
from operators_one_operator_per_file import _helpers as H


def compute(a, b):
    """True if 0 ≤ aₙ ≤ bₙ for every term, so Σbₙ converging makes Σaₙ converge"""
    return len(a) == len(b) and all(0 <= x <= y for x, y in zip(a, b))
