"""Tangent vector   [v ∈ TₚM]

Category : Math > Differential geometry and tensors
Formula  : The velocity vector of a curve through p on a manifold

Status   : ready to use - call compute(curve, t)
"""

NAME = 'Tangent vector'
SYMBOL = 'v ∈ TₚM'
CATEGORY = 'Math'
SUBCATEGORY = 'Differential geometry and tensors'
FORMULA = 'The velocity vector of a curve through p on a manifold'
import math
from operators_one_operator_per_file import _helpers as H


def compute(curve, t):
    """The velocity vector of a curve γ(t) at t  (type the curve as a list, e.g. [cos(t), sin(t)])"""
    h = 1e-6
    return [(p - m) / (2 * h) for p, m in zip(curve(t + h), curve(t - h))]
