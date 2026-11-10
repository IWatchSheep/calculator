"""Gravitational time dilation: from the horizon   [Δt₀ = Δt√(1 − rₛ/r)]

Category : Physics > Physics
Formula  : Δt₀ = Δt √(1 − rₛ/r)   (rₛ is the answer of the row above; r > rₛ)

Status   : ready to use - call compute(dt, rs, r)
"""
import math

NAME = 'Gravitational time dilation: from the horizon'
SYMBOL = 'Δt₀ = Δt√(1 − rₛ/r)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'Δt₀ = Δt √(1 − rₛ/r)   (rₛ is the answer of the row above; r > rₛ)'


def compute(dt, rs, r):
    """Δt₀ = Δt √(1 − rₛ/r)   (r > rₛ)"""
    if r <= rs:
        raise ValueError('r must be outside the Schwarzschild radius')
    return dt * math.sqrt(1 - rs / r)
