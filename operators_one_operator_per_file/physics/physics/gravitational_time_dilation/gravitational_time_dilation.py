"""Gravitational time dilation   [Δt₀ = Δt√(1 − rₛ/r)]

Category : Physics > Physics
Formula  : Δt₀ = Δt √(1 − 2GM/(r c²))   (clock at distance r from mass M, r > rₛ)

Status   : ready to use - call compute(dt, M, r, G, c)
"""
import math

NAME = 'Gravitational time dilation'
SYMBOL = 'Δt₀ = Δt√(1 − rₛ/r)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'Δt₀ = Δt √(1 − 2GM/(r c²))   (clock at distance r from mass M, r > rₛ)'


def compute(dt, M, r, G=6.674e-11, c=299792458):
    """Δt₀ = Δt √(1 − 2GM/(r c²))   (clock at distance r from mass M, r > rₛ)"""
    if r <= 2 * G * M / c ** 2:
        raise ValueError('r must be outside the Schwarzschild radius')
    return dt * math.sqrt(1 - 2 * G * M / (r * c ** 2))
