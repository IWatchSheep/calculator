"""Impulse   [J = FΔt]

Category : Physics > Physics
Formula  : J = F Δt

Status   : ready to use - call compute(F, dt)
"""

NAME = 'Impulse'
SYMBOL = 'J = FΔt'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'J = F Δt'


def compute(F, dt):
    """J = F Δt"""
    return F * dt
