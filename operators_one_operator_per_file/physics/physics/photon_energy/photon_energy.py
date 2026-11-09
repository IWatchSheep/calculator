"""Photon energy (Planck's relation)   [E = hf]

Category : Physics > Physics
Formula  : E = h f   (h = 6.62607015×10⁻³⁴ J·s)

Status   : ready to use - call compute(f, h)
"""
import math

NAME = "Photon energy (Planck's relation)"
SYMBOL = 'E = hf'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'E = h f   (h = 6.62607015×10⁻³⁴ J·s)'


def compute(f, h=6.62607015e-34):
    """E = h f   (h = 6.62607015×10⁻³⁴ J·s)"""
    return h * f
