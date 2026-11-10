"""Complementary filter   [α(θ + ωt) + (1 − α)θₘ]

Category : Physics > Physics
Formula  : θ = α (θ₀ + ω t) + (1 − α) θₘ   (the gyro prediction blended with a measured angle; α close to 1 trusts the gyro)

Status   : ready to use - call compute(previous, gyro, dt, measured, alpha)
"""
import math

NAME = 'Complementary filter'
SYMBOL = 'α(θ + ωt) + (1 − α)θₘ'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'θ = α (θ₀ + ω t) + (1 − α) θₘ   (the gyro prediction blended with a measured angle; α close to 1 trusts the gyro)'


def compute(previous, gyro, dt, measured, alpha):
    """θ = α (θ₀ + ω t) + (1 − α) θₘ, radians"""
    if dt <= 0:
        raise ValueError("time step must be positive")
    if not 0 <= alpha <= 1:
        raise ValueError("the weight must be from 0 to 1")
    return alpha * (previous + gyro * dt) + (1 - alpha) * measured
