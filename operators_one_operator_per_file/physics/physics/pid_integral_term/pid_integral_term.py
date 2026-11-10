"""PID integral term   [Iout = Ki (I + e t)]

Category : Physics > Physics
Formula  : Iout = Ki (I + e t)   (the integral contribution: this step's error is added before multiplying by Ki)

Status   : ready to use - call compute(ki, integral, error, dt)
"""
import math

NAME = 'PID integral term'
SYMBOL = 'Iout = Ki (I + e t)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = "Iout = Ki (I + e t)   (the integral contribution: this step's error is added before multiplying by Ki)"


def compute(ki, integral, error, dt):
    """Iout = Ki (I + e t)"""
    if dt <= 0:
        raise ValueError("time step must be positive")
    return ki * (integral + error * dt)
