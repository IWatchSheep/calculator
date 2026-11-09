"""Particle in a box (energy levels)   [Eₙ = n²h²/8mL²]

Category : Physics > Physics
Formula  : Eₙ = n² h² / (8 m L²)   (h = 6.62607015×10⁻³⁴ J·s)

Status   : ready to use - call compute(n, m, L, h)
"""
import math

NAME = 'Particle in a box (energy levels)'
SYMBOL = 'Eₙ = n²h²/8mL²'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'Eₙ = n² h² / (8 m L²)   (h = 6.62607015×10⁻³⁴ J·s)'


def compute(n, m, L, h=6.62607015e-34):
    """Eₙ = n² h² / (8 m L²)   (h = 6.62607015×10⁻³⁴ J·s)"""
    return n ** 2 * h ** 2 / (8 * m * L ** 2)
