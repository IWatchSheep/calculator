"""Compton wavelength shift   [Δλ = (h/mc)(1 − cos θ)]

Category : Physics > Physics
Formula  : Δλ = h / (m c) × (1 − cos θ)   (scattering off an electron by default)

Status   : ready to use - call compute(theta, m, h, c)
"""
import math

NAME = 'Compton wavelength shift'
SYMBOL = 'Δλ = (h/mc)(1 − cos θ)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'Δλ = h / (m c) × (1 − cos θ)   (scattering off an electron by default)'


def compute(theta, m=9.1093837015e-31, h=6.62607015e-34, c=299792458):
    """Δλ = h / (m c) × (1 − cos θ)   (scattering off an electron by default)"""
    return h / (m * c) * (1 - math.cos(theta))
