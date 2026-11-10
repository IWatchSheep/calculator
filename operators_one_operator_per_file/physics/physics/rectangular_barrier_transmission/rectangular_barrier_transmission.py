"""Rectangular-barrier transmission   [T = [1 + V² sinh²(κ L) / (4 E (V − E))]⁻¹]

Category : Physics > Physics
Formula  : T = [1 + V² sinh²(κ L) / (4 E (V − E))]⁻¹, κ = √(2 m (V − E)) / ħ   (the probability that a particle of mass m and energy E below a barrier of height V and thickness L gets through; ħ = 1.054571817e-34 J s unless another is passed)

Status   : ready to use - call compute(E, V, L, m, hbar=1.054571817e-34)
"""
import math

NAME = 'Rectangular-barrier transmission'
SYMBOL = 'T = [1 + V² sinh²(κ L) / (4 E (V − E))]⁻¹'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'T = [1 + V² sinh²(κ L) / (4 E (V − E))]⁻¹, κ = √(2 m (V − E)) / ħ   (the probability that a particle of mass m and energy E below a barrier of height V and thickness L gets through; ħ = 1.054571817e-34 J s unless another is passed)'


def compute(E, V, L, m, hbar=1.054571817e-34):
    """transmission probability, from 0 to 1"""
    if E <= 0:
        raise ValueError("the energy must be positive")
    if E >= V:
        raise ValueError("the energy is not below the barrier")
    if L <= 0:
        raise ValueError("a length must be positive")
    if m <= 0:
        raise ValueError("mass must be positive")
    if hbar <= 0:
        raise ValueError("hbar must be positive")
    kappa = math.sqrt(2 * m * (V - E)) / hbar
    try:
        s = math.sinh(kappa * L)
    except OverflowError:          # a barrier this thick lets nothing through
        return 0.0
    return 1 / (1 + V ** 2 * s ** 2 / (4 * E * (V - E)))
