"""Lagrange interpolation   [L(x)]

Category : Math > Optimization and numerical methods
Formula  : L(x) = Σᵢ yᵢ ∏_{j≠i} (x − xⱼ) / (xᵢ − xⱼ)

Status   : ready to use - call compute(xs, ys, x)
"""
import math

NAME = 'Lagrange interpolation'
SYMBOL = 'L(x)'
CATEGORY = 'Math'
SUBCATEGORY = 'Optimization and numerical methods'
FORMULA = 'L(x) = Σᵢ yᵢ ∏_{j≠i} (x − xⱼ) / (xᵢ − xⱼ)'


def compute(xs, ys, x):
    """L(x) = Σᵢ yᵢ ∏_{j≠i} (x − xⱼ) / (xᵢ − xⱼ)"""
    return sum(ys[i] * math.prod((x - xs[j]) / (xs[i] - xs[j]) for j in range(len(xs)) if j != i) for i in range(len(xs)))
