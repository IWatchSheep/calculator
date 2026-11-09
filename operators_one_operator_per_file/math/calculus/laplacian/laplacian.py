"""Laplacian   [Δ]

Category : Math > Calculus
Formula  : Δf = ∂²f/∂x² + ∂²f/∂y² + ∂²f/∂z²

Status   : ready to use - call compute(f, point)
"""

NAME = 'Laplacian'
SYMBOL = 'Δ'
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = 'Δf = ∂²f/∂x² + ∂²f/∂y² + ∂²f/∂z²'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, point):
    """Δf = sum of the second partial derivatives at a point"""
    return sum(H.partial2(f, point, i, i) for i in range(len(point)))
