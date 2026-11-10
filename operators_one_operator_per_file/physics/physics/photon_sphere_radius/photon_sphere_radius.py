"""Photon sphere   [r = 3GM/c² = 1.5 Rs]

Category : Physics > Physics
Formula  : r = 3GM/c² = 1.5 Rs   (the radius of the unstable circular orbit of a light ray)

Status   : ready to use - call compute(Rs)
"""
import math

NAME = 'Photon sphere'
SYMBOL = 'r = 3GM/c² = 1.5 Rs'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'r = 3GM/c² = 1.5 Rs   (the radius of the unstable circular orbit of a light ray)'


def compute(Rs):
    """r = 1.5 Rs"""
    if Rs <= 0:
        raise ValueError("the horizon radius must be positive")
    return 1.5 * Rs
