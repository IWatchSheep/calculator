"""Circular-orbit local speed   [v = c √((Rs/2r) / (1 − Rs/r))]

Category : Physics > Physics
Formula  : v = c √( (Rs / (2 r)) / (1 − Rs / r) )   (the speed an observer hovering at that radius measures; stable orbits only, r ≥ 3 Rs)

Status   : ready to use - call compute(r, Rs)
"""
import math

NAME = 'Circular-orbit local speed'
SYMBOL = 'v = c √((Rs/2r) / (1 − Rs/r))'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'v = c √( (Rs / (2 r)) / (1 − Rs / r) )   (the speed an observer hovering at that radius measures; stable orbits only, r ≥ 3 Rs)'


def compute(r, Rs):
    """v = c √((Rs / (2 r)) / (1 − Rs / r)), metres per second"""
    if r <= 0:
        raise ValueError("a radius must be positive")
    if Rs <= 0:
        raise ValueError("the horizon radius must be positive")
    if r < 3 * Rs:
        raise ValueError("no stable circular orbit inside the ISCO")
    return 299792458 * math.sqrt((Rs / (2 * r)) / (1 - Rs / r))
