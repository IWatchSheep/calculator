"""Hydrostatic pressure   [P = ρgh]

Category : Physics > Physics
Formula  : P = ρ g h   (pressure due to the fluid alone, g = 9.81 m/s²)

Status   : ready to use - call compute(rho, h, g)
"""
import math

NAME = 'Hydrostatic pressure'
SYMBOL = 'P = ρgh'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'P = ρ g h   (pressure due to the fluid alone, g = 9.81 m/s²)'


def compute(rho, h, g=9.81):
    """P = ρ g h   (pressure due to the fluid alone, g = 9.81 m/s²)"""
    return rho * g * h
