"""Cylinder moment of inertia   [I = ½ M R²]

Category : Physics > Physics
Formula  : I = ½ M R²   (a solid cylinder or disc about its own centre axis)

Status   : ready to use - call compute(mass, radius)
"""
import math

NAME = 'Cylinder moment of inertia'
SYMBOL = 'I = ½ M R²'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'I = ½ M R²   (a solid cylinder or disc about its own centre axis)'


def compute(mass, radius):
    """I = ½ M R²"""
    if mass <= 0:
        raise ValueError("mass must be positive")
    if radius < 0:
        raise ValueError("radius cannot be negative")
    return 0.5 * mass * radius * radius
