"""Schwarzschild radius   [rₛ = 2GM/c²]

Category : Physics > Physics
Formula  : rₛ = 2 G M / c²   (G = 6.674×10⁻¹¹ N·m²/kg²)

Status   : ready to use - call compute(M, G, c)
"""
import math

NAME = 'Schwarzschild radius'
SYMBOL = 'rₛ = 2GM/c²'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'rₛ = 2 G M / c²   (G = 6.674×10⁻¹¹ N·m²/kg²)'


def compute(M, G=6.674e-11, c=299792458):
    """rₛ = 2 G M / c²   (G = 6.674×10⁻¹¹ N·m²/kg²)"""
    return 2 * G * M / c ** 2
