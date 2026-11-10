"""Lense–Thirring rate   [Ω = 2GJ / (c² r³)]

Category : Physics > Physics
Formula  : Ω = 2 G J / (c² r³)   (radians per second by which local inertial frames are dragged around a slowly spinning mass; G = 6.674e-11, c = 299792458; positive J is a right-hand spin)

Status   : ready to use - call compute(J, r, G=6.674e-11, c=299792458)
"""
import math

NAME = 'Lense–Thirring rate'
SYMBOL = 'Ω = 2GJ / (c² r³)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'Ω = 2 G J / (c² r³)   (radians per second by which local inertial frames are dragged around a slowly spinning mass; G = 6.674e-11, c = 299792458; positive J is a right-hand spin)'


def compute(J, r, G=6.674e-11, c=299792458):
    """Ω = 2 G J / (c² r³), radians per second (slow-spin limit)"""
    if r <= 0:
        raise ValueError("a radius must be positive")
    return 2 * G * J / (c * c * (r * r * r))
