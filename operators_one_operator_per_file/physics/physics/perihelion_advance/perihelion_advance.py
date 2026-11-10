"""Perihelion advance   [3π Rs / (a (1 − e²)) per orbit]

Category : Physics > Physics
Formula  : 3π Rs / (a (1 − e²)) radians per orbit, times 36525 / period_days orbits per century, times 648000/π: arcseconds per century (the general-relativity part only, not the pull of other planets)

Status   : ready to use - call compute(a, eccentricity, period_days, Rs)
"""
import math

NAME = 'Perihelion advance'
SYMBOL = '3π Rs / (a (1 − e²)) per orbit'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = '3π Rs / (a (1 − e²)) radians per orbit, times 36525 / period_days orbits per century, times 648000/π: arcseconds per century (the general-relativity part only, not the pull of other planets)'


def compute(a, eccentricity, period_days, Rs):
    """the relativistic perihelion advance in arcseconds per century (Julian century of 36525 days)"""
    if a <= 0:
        raise ValueError("a radius must be positive")
    if period_days <= 0:
        raise ValueError("the period must be positive")
    if Rs <= 0:
        raise ValueError("the horizon radius must be positive")
    if not 0 <= eccentricity < 1:
        raise ValueError("the eccentricity must be from 0 up to but not including 1")
    return 3 * math.pi * Rs / (a * (1 - eccentricity * eccentricity)) * (36525 / period_days) * (648000 / math.pi)
