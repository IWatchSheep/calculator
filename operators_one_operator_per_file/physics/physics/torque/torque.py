"""Torque   [τ = rF·sin θ]

Category : Physics > Physics
Formula  : τ = r F sin θ

Status   : ready to use - call compute(r, F, theta)
"""
import math

NAME = 'Torque'
SYMBOL = 'τ = rF·sin θ'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'τ = r F sin θ'


def compute(r, F, theta):
    """τ = r F sin θ"""
    return r * F * math.sin(theta)
