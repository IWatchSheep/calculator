"""Photon momentum   [p = h/λ]

Category : Physics > Physics
Formula  : p = h / λ   (h = 6.62607015×10⁻³⁴ J·s)

Status   : ready to use - call compute(wavelength, h)
"""
import math

NAME = 'Photon momentum'
SYMBOL = 'p = h/λ'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'p = h / λ   (h = 6.62607015×10⁻³⁴ J·s)'


def compute(wavelength, h=6.62607015e-34):
    """p = h / λ   (h = 6.62607015×10⁻³⁴ J·s)"""
    return h / wavelength
