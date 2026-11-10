"""Circular-orbit coordinate speed   [r Ω = c √(Rs / (2 r))]

Category : Physics > Physics
Formula  : r Ω = c √(Rs / (2 r))   (the Kepler speed of a circular orbit: circumference radius times the angular speed; not the speed a hovering observer measures; r > 1.5 Rs)

Status   : ready to use - call compute(r, Rs)
"""
import math

NAME = 'Circular-orbit coordinate speed'
SYMBOL = 'r Ω = c √(Rs / (2 r))'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'r Ω = c √(Rs / (2 r))   (the Kepler speed of a circular orbit: circumference radius times the angular speed; not the speed a hovering observer measures; r > 1.5 Rs)'


def compute(r, Rs):
    """r Ω = c √(Rs / (2 r)), metres per second"""
    if r <= 0:
        raise ValueError("a radius must be positive")
    if Rs <= 0:
        raise ValueError("the horizon radius must be positive")
    if r <= 1.5 * Rs:
        raise ValueError("no circular orbit for a massive particle on or inside the photon sphere")
    return 299792458 * math.sqrt(Rs / (2 * r))
