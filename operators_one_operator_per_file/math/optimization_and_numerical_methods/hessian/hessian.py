"""Hessian   [H]

Category : Math > Optimization and numerical methods
Formula  : Hᵢⱼ = ∂²f / ∂xᵢ∂xⱼ  (matrix of second partial derivatives)

Status   : ready to use - call compute(f, point)
"""

NAME = 'Hessian'
SYMBOL = 'H'
CATEGORY = 'Math'
SUBCATEGORY = 'Optimization and numerical methods'
FORMULA = 'Hᵢⱼ = ∂²f / ∂xᵢ∂xⱼ  (matrix of second partial derivatives)'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, point):
    """Hᵢⱼ = ∂²f/∂xᵢ∂xⱼ at a point"""
    n = len(point)
    return [[H.partial2(f, point, i, j) for j in range(n)] for i in range(n)]
