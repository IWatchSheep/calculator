"""Self-induced emf of an inductor   [ε = −L ΔI/Δt]

Category : Physics > Physics
Formula  : ε = −L ΔI / Δt

Status   : ready to use - call compute(L, delta_I, dt)
"""
import math

NAME = 'Self-induced emf of an inductor'
SYMBOL = 'ε = −L ΔI/Δt'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'ε = −L ΔI / Δt'


def compute(L, delta_I, dt):
    """ε = −L ΔI / Δt"""
    return -L * delta_I / dt
