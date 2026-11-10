"""PID derivative   [D = Kd (e − e₀) / t]

Category : Physics > Physics
Formula  : D = Kd (e − e₀) / t   (the derivative contribution)

Status   : ready to use - call compute(kd, error, previous_error, dt)
"""
import math

NAME = 'PID derivative'
SYMBOL = 'D = Kd (e − e₀) / t'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'D = Kd (e − e₀) / t   (the derivative contribution)'


def compute(kd, error, previous_error, dt):
    """D = Kd (e − e₀) / t"""
    if dt <= 0:
        raise ValueError("time step must be positive")
    return kd * (error - previous_error) / dt
