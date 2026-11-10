"""Tree impact force   [F = mv² / 2s]

Category : Physics > Physics
Formula  : F = m v² / (2 s)   (the average force to stop a mass from speed v over a distance s)

Status   : ready to use - call compute(mass, speed, distance)
"""
import math

NAME = 'Tree impact force'
SYMBOL = 'F = mv² / 2s'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'F = m v² / (2 s)   (the average force to stop a mass from speed v over a distance s)'


def compute(mass, speed, distance):
    """F = m v² / (2 s)"""
    if mass <= 0:
        raise ValueError("mass must be positive")
    if distance <= 0:
        raise ValueError("the stopping distance must be positive")
    return mass * speed * speed / (2 * distance)
