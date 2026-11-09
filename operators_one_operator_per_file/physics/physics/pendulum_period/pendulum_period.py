"""Pendulum period   [T = 2π√(L/g)]

Category : Physics > Physics
Formula  : T = 2π √(L / g)

Status   : ready to use - call compute(L, g=9.81)
"""
import math

NAME = 'Pendulum period'
SYMBOL = 'T = 2π√(L/g)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'T = 2π √(L / g)'


def compute(L, g=9.81):
    """T = 2π √(L / g)"""
    return 2 * math.pi * math.sqrt(L / g)
