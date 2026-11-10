"""PID integral state   [I ← I + e t]

Category : Physics > Physics
Formula  : I ← I + e t   (the stored integral the robot keeps for the next step; not part of the four-row sum)

Status   : ready to use - call compute(integral, error, dt)
"""
import math

NAME = 'PID integral state'
SYMBOL = 'I ← I + e t'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'I ← I + e t   (the stored integral the robot keeps for the next step; not part of the four-row sum)'


def compute(integral, error, dt):
    """I + e t"""
    if dt <= 0:
        raise ValueError("time step must be positive")
    return integral + error * dt
