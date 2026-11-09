"""Heisenberg uncertainty principle   [Δx·Δp ≥ ħ/2]

Category : Physics > Physics
Formula  : Δp ≥ ħ / (2 Δx)   (returns the smallest possible Δp)

Status   : ready to use - call compute(delta_x, hbar)
"""
import math

NAME = 'Heisenberg uncertainty principle'
SYMBOL = 'Δx·Δp ≥ ħ/2'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'Δp ≥ ħ / (2 Δx)   (returns the smallest possible Δp)'


def compute(delta_x, hbar=1.054571817e-34):
    """Δp ≥ ħ / (2 Δx)   (returns the smallest possible Δp)"""
    return hbar / (2 * delta_x)
