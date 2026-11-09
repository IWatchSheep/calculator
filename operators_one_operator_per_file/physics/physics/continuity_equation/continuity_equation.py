"""Continuity equation   [A₁v₁ = A₂v₂]

Category : Physics > Physics
Formula  : v₂ = A₁ v₁ / A₂   (incompressible fluid)

Status   : ready to use - call compute(A1, v1, A2)
"""
import math

NAME = 'Continuity equation'
SYMBOL = 'A₁v₁ = A₂v₂'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'v₂ = A₁ v₁ / A₂   (incompressible fluid)'


def compute(A1, v1, A2):
    """v₂ = A₁ v₁ / A₂   (incompressible fluid)"""
    return A1 * v1 / A2
