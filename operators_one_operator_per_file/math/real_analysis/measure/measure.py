"""Measure   [μ]

Category : Math > Real analysis
Formula  : A function assigning size to sets: μ(∅) = 0 and countably additive on disjoint sets

Status   : ready to use - call compute(intervals)
"""

NAME = 'Measure'
SYMBOL = 'μ'
CATEGORY = 'Math'
SUBCATEGORY = 'Real analysis'
FORMULA = 'A function assigning size to sets: μ(∅) = 0 and countably additive on disjoint sets'
import math
from operators_one_operator_per_file import _helpers as H


def compute(intervals):
    """Total length of a union of intervals [(a, b), …]  (overlaps counted once)"""
    total, end = 0.0, None
    for a, b in sorted(intervals):
        if end is None or a > end:
            total += b - a
            end = b
        elif b > end:
            total += b - end
            end = b
    return total
