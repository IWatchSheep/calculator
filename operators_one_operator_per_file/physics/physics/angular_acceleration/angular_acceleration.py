"""Angular acceleration   [α = τ / I]

Category : Physics > Physics
Formula  : α = τ / I   (a negative torque turns the other way)

Status   : ready to use - call compute(torque, inertia)
"""
import math

NAME = 'Angular acceleration'
SYMBOL = 'α = τ / I'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'α = τ / I   (a negative torque turns the other way)'


def compute(torque, inertia):
    """α = τ / I"""
    if inertia <= 0:
        raise ValueError("the moment of inertia must be positive")
    return torque / inertia
