"""Double-slit fringe spacing   [Δy = λL/d]

Category : Physics > Physics
Formula  : Δy = λ L / d   (small angles)

Status   : ready to use - call compute(wavelength, L, d)
"""
import math

NAME = 'Double-slit fringe spacing'
SYMBOL = 'Δy = λL/d'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'Δy = λ L / d   (small angles)'


def compute(wavelength, L, d):
    """Δy = λ L / d   (small angles)"""
    return wavelength * L / d
