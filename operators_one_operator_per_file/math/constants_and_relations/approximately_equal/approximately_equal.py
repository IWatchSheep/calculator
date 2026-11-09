"""Approximately equal   [≈]

Category : Math > Constants and relations
Formula  : a ≈ b  (equal within a small tolerance)

Status   : ready to use - call compute(a, b, rel_tol=1e-9)
"""
import math

NAME = 'Approximately equal'
SYMBOL = '≈'
CATEGORY = 'Math'
SUBCATEGORY = 'Constants and relations'
FORMULA = 'a ≈ b  (equal within a small tolerance)'


def compute(a, b, rel_tol=1e-9):
    """a ≈ b  (equal within a small tolerance)"""
    return math.isclose(a, b, rel_tol=rel_tol)
