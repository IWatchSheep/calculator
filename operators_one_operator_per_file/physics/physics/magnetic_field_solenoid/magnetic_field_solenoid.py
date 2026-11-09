"""Magnetic field inside a solenoid   [B = μ₀nI]

Category : Physics > Physics
Formula  : B = μ₀ n I   (n = turns per metre, μ₀ = 4π×10⁻⁷ T·m/A)

Status   : ready to use - call compute(n, I, mu0)
"""
import math

NAME = 'Magnetic field inside a solenoid'
SYMBOL = 'B = μ₀nI'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'B = μ₀ n I   (n = turns per metre, μ₀ = 4π×10⁻⁷ T·m/A)'


def compute(n, I, mu0=4 * math.pi * 1e-7):
    """B = μ₀ n I   (n = turns per metre, μ₀ = 4π×10⁻⁷ T·m/A)"""
    return mu0 * n * I
