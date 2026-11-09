"""Reynolds number   [Re = ρvL/μ]

Category : Physics > Physics
Formula  : Re = ρ v L / μ   (μ = dynamic viscosity)

Status   : ready to use - call compute(rho, v, L, mu)
"""
import math

NAME = 'Reynolds number'
SYMBOL = 'Re = ρvL/μ'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'Re = ρ v L / μ   (μ = dynamic viscosity)'


def compute(rho, v, L, mu):
    """Re = ρ v L / μ   (μ = dynamic viscosity)"""
    return rho * v * L / mu
