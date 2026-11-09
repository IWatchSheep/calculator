"""Diffraction grating   [d sin θ = mλ]

Category : Physics > Physics
Formula  : θ = arcsin(m λ / d)   (angle in radians)

Status   : ready to use - call compute(m, wavelength, d)
"""
import math

NAME = 'Diffraction grating'
SYMBOL = 'd sin θ = mλ'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'θ = arcsin(m λ / d)   (angle in radians)'


def compute(m, wavelength, d):
    """θ = arcsin(m λ / d)   (angle in radians)"""
    if abs(m * wavelength / d) > 1:
        raise ValueError('this order does not exist')
    return math.asin(m * wavelength / d)
