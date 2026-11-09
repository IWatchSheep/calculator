"""Fourier series   [Σ aₙcos + bₙsin]

Category : Math > Transforms and differential equations
Formula  : f(x) = a₀/2 + Σ (aₙ cos nx + bₙ sin nx),  aₙ = (1/π)∫f cos nx dx,  bₙ = (1/π)∫f sin nx dx

Status   : ready to use - call compute(f, n)
"""

NAME = 'Fourier series'
SYMBOL = 'Σ aₙcos + bₙsin'
CATEGORY = 'Math'
SUBCATEGORY = 'Transforms and differential equations'
FORMULA = 'f(x) = a₀/2 + Σ (aₙ cos nx + bₙ sin nx),  aₙ = (1/π)∫f cos nx dx,  bₙ = (1/π)∫f sin nx dx'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, n):
    """The Fourier coefficients (aₙ, bₙ) of f on [−π, π]; type f with x"""
    n = int(n)
    a = H.simpson(lambda x: f(x) * math.cos(n * x), -math.pi, math.pi, 4000) / math.pi
    b = H.simpson(lambda x: f(x) * math.sin(n * x), -math.pi, math.pi, 4000) / math.pi
    return a, b
