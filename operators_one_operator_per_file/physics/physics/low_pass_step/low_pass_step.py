"""Low-pass step   [y + (t/(t+τ))(x − y)]

Category : Physics > Physics
Formula  : y + (t / (t + τ)) (x − y)   (one step of a low-pass filter with time constant τ; the weight is t / (t + τ), not a typed α)

Status   : ready to use - call compute(previous, sample, dt, tau)
"""
import math

NAME = 'Low-pass step'
SYMBOL = 'y + (t/(t+τ))(x − y)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'y + (t / (t + τ)) (x − y)   (one step of a low-pass filter with time constant τ; the weight is t / (t + τ), not a typed α)'


def compute(previous, sample, dt, tau):
    """y + (t / (t + τ)) (x − y)"""
    if dt <= 0:
        raise ValueError("time step must be positive")
    if tau <= 0:
        raise ValueError("the time constant must be positive")
    return previous + dt / (dt + tau) * (sample - previous)
