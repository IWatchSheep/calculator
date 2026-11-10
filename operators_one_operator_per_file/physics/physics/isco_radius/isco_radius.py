"""Innermost stable circular orbit   [r = 6GM/c² = 3 Rs]

Category : Physics > Physics
Formula  : r = 6GM/c² = 3 Rs   (the closest stable circular orbit of a massive particle around a non-spinning mass)

Status   : ready to use - call compute(Rs)
"""
import math

NAME = 'Innermost stable circular orbit'
SYMBOL = 'r = 6GM/c² = 3 Rs'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'r = 6GM/c² = 3 Rs   (the closest stable circular orbit of a massive particle around a non-spinning mass)'


def compute(Rs):
    """r = 3 Rs"""
    if Rs <= 0:
        raise ValueError("the horizon radius must be positive")
    return 3 * Rs
