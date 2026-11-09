"""Buoyant force (Archimedes' principle)   [F = ρgV]

Category : Physics > Physics
Formula  : F = ρ g V   (g = 9.81 m/s²)

Status   : ready to use - call compute(rho, V, g)
"""
import math

NAME = "Buoyant force (Archimedes' principle)"
SYMBOL = 'F = ρgV'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'F = ρ g V   (g = 9.81 m/s²)'


def compute(rho, V, g=9.81):
    """F = ρ g V   (g = 9.81 m/s²)"""
    return rho * g * V
