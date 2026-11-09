"""Faraday's law of induction   [ε = −N ΔΦ/Δt]

Category : Physics > Physics
Formula  : ε = −N ΔΦ / Δt

Status   : ready to use - call compute(N, delta_flux, dt)
"""
import math

NAME = "Faraday's law of induction"
SYMBOL = 'ε = −N ΔΦ/Δt'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'ε = −N ΔΦ / Δt'


def compute(N, delta_flux, dt):
    """ε = −N ΔΦ / Δt"""
    return -N * delta_flux / dt
