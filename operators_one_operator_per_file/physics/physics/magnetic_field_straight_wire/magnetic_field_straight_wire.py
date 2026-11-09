"""Magnetic field of a straight wire   [B = μ₀I/2πr]

Category : Physics > Physics
Formula  : B = μ₀ I / (2π r)   (μ₀ = 4π×10⁻⁷ T·m/A)

Status   : ready to use - call compute(I, r, mu0)
"""
import math

NAME = 'Magnetic field of a straight wire'
SYMBOL = 'B = μ₀I/2πr'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'B = μ₀ I / (2π r)   (μ₀ = 4π×10⁻⁷ T·m/A)'


def compute(I, r, mu0=4 * math.pi * 1e-7):
    """B = μ₀ I / (2π r)   (μ₀ = 4π×10⁻⁷ T·m/A)"""
    return mu0 * I / (2 * math.pi * r)
