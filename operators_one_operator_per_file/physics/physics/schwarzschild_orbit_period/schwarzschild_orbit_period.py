"""Circular-orbit period   [T = 2π / Ω]

Category : Physics > Physics
Formula  : T = 2π / Ω   (the coordinate-time period of a circular orbit around a non-spinning mass; r > 1.5 Rs)

Status   : ready to use - call compute(r, Rs)
"""
import math

NAME = 'Circular-orbit period'
SYMBOL = 'T = 2π / Ω'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'T = 2π / Ω   (the coordinate-time period of a circular orbit around a non-spinning mass; r > 1.5 Rs)'


def compute(r, Rs):
    """T = 2π / Ω, seconds of coordinate time"""
    if r <= 0:
        raise ValueError("a radius must be positive")
    if Rs <= 0:
        raise ValueError("the horizon radius must be positive")
    if r <= 1.5 * Rs:
        raise ValueError("no circular orbit for a massive particle on or inside the photon sphere")
    return 2 * math.pi / (299792458 * math.sqrt(Rs / (2 * r * r * r)))
