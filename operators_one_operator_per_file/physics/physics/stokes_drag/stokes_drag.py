"""Stokes' drag force   [F = 6πμrv]

Category : Physics > Physics
Formula  : F = 6π μ r v   (small sphere, slow flow)

Status   : ready to use - call compute(mu, r, v)
"""
import math

NAME = "Stokes' drag force"
SYMBOL = 'F = 6πμrv'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'F = 6π μ r v   (small sphere, slow flow)'


def compute(mu, r, v):
    """F = 6π μ r v   (small sphere, slow flow)"""
    return 6 * math.pi * mu * r * v
