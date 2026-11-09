"""Bernoulli's equation   [P + ½ρv² + ρgh = const]

Category : Physics > Physics
Formula  : P₂ = P₁ + ½ρ(v₁² − v₂²) + ρg(h₁ − h₂)   (g = 9.81 m/s²)

Status   : ready to use - call compute(P1, v1, h1, v2, h2, rho, g)
"""
import math

NAME = "Bernoulli's equation"
SYMBOL = 'P + ½ρv² + ρgh = const'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'P₂ = P₁ + ½ρ(v₁² − v₂²) + ρg(h₁ − h₂)   (g = 9.81 m/s²)'


def compute(P1, v1, h1, v2, h2, rho, g=9.81):
    """P₂ = P₁ + ½ρ(v₁² − v₂²) + ρg(h₁ − h₂)   (g = 9.81 m/s²)"""
    return P1 + 0.5 * rho * (v1 ** 2 - v2 ** 2) + rho * g * (h1 - h2)
