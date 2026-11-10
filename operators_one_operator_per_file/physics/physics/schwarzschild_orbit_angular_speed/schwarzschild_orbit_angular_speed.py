"""Circular-orbit angular speed   [Ω = c √(Rs / (2 r³))]

Category : Physics > Physics
Formula  : Ω = c √(Rs / (2 r³))   (radians per second of coordinate time for a circular orbit around a non-spinning mass; the Kepler form; r > 1.5 Rs; c = 299792458 m/s)

Status   : ready to use - call compute(r, Rs)
"""
import math

NAME = 'Circular-orbit angular speed'
SYMBOL = 'Ω = c √(Rs / (2 r³))'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'Ω = c √(Rs / (2 r³))   (radians per second of coordinate time for a circular orbit around a non-spinning mass; the Kepler form; r > 1.5 Rs; c = 299792458 m/s)'


def compute(r, Rs):
    """Ω = c √(Rs / (2 r³)), radians per second of coordinate time"""
    if r <= 0:
        raise ValueError("a radius must be positive")
    if Rs <= 0:
        raise ValueError("the horizon radius must be positive")
    if r <= 1.5 * Rs:
        raise ValueError("no circular orbit for a massive particle on or inside the photon sphere")
    return 299792458 * math.sqrt(Rs / (2 * r * r * r))
