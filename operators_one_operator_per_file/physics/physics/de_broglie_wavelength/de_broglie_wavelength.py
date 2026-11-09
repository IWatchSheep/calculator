"""de Broglie wavelength   [λ = h/mv]

Category : Physics > Physics
Formula  : λ = h / (m v)   (h = 6.62607015×10⁻³⁴ J·s, non-relativistic)

Status   : ready to use - call compute(m, v, h)
"""
import math

NAME = 'de Broglie wavelength'
SYMBOL = 'λ = h/mv'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'λ = h / (m v)   (h = 6.62607015×10⁻³⁴ J·s, non-relativistic)'


def compute(m, v, h=6.62607015e-34):
    """λ = h / (m v)   (h = 6.62607015×10⁻³⁴ J·s, non-relativistic)"""
    return h / (m * v)
