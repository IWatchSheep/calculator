"""Poiseuille's law (flow in a pipe)   [Q = πr⁴ΔP/8μL]

Category : Physics > Physics
Formula  : Q = π r⁴ ΔP / (8 μ L)   (laminar flow in a round pipe)

Status   : ready to use - call compute(r, delta_P, mu, L)
"""
import math

NAME = "Poiseuille's law (flow in a pipe)"
SYMBOL = 'Q = πr⁴ΔP/8μL'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'Q = π r⁴ ΔP / (8 μ L)   (laminar flow in a round pipe)'


def compute(r, delta_P, mu, L):
    """Q = π r⁴ ΔP / (8 μ L)   (laminar flow in a round pipe)"""
    return math.pi * r ** 4 * delta_P / (8 * mu * L)
