"""Hydraulic press (Pascal's principle)   [F₂ = F₁A₂/A₁]

Category : Physics > Physics
Formula  : F₂ = F₁ A₂ / A₁   (pressure is the same everywhere in the fluid)

Status   : ready to use - call compute(F1, A1, A2)
"""
import math

NAME = "Hydraulic press (Pascal's principle)"
SYMBOL = 'F₂ = F₁A₂/A₁'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'F₂ = F₁ A₂ / A₁   (pressure is the same everywhere in the fluid)'


def compute(F1, A1, A2):
    """F₂ = F₁ A₂ / A₁   (pressure is the same everywhere in the fluid)"""
    return F1 * A2 / A1
