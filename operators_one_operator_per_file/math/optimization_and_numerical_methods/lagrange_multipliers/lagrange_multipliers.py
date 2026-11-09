"""Lagrange multipliers   [∇f = λ∇g]

Category : Math > Optimization and numerical methods
Formula  : Extrema of f subject to g = 0 occur where ∇f = λ ∇g

Status   : ready to use - call compute(f, g, point)
"""

NAME = 'Lagrange multipliers'
SYMBOL = '∇f = λ∇g'
CATEGORY = 'Math'
SUBCATEGORY = 'Optimization and numerical methods'
FORMULA = 'Extrema of f subject to g = 0 occur where ∇f = λ ∇g'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, g, point):
    """At a point: the λ that best fits ∇f = λ∇g, and how far off it is → (λ, error); error ≈ 0 means a candidate extremum"""
    gf = [H.partial(f, point, i) for i in range(len(point))]
    gg = [H.partial(g, point, i) for i in range(len(point))]
    denom = sum(v * v for v in gg)
    if denom == 0:
        raise ValueError("∇g is zero here")
    lam = sum(a * b for a, b in zip(gf, gg)) / denom
    return lam, math.sqrt(sum((a - lam * b) ** 2 for a, b in zip(gf, gg)))
