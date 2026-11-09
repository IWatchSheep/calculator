"""Partial derivative   [∂/∂x]

Category : Math > Calculus
Formula  : ∂f/∂xᵢ ≈ (f(…xᵢ+h…) − f(…xᵢ−h…)) / 2h   (point is a list, i is the variable index)

Status   : ready to use - call compute(f, point, i, h=1e-6)
"""

NAME = 'Partial derivative'
SYMBOL = '∂/∂x'
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = '∂f/∂xᵢ ≈ (f(…xᵢ+h…) − f(…xᵢ−h…)) / 2h   (point is a list, i is the variable index)'


def compute(f, point, i, h=1e-6):
    """∂f/∂xᵢ ≈ (f(…xᵢ+h…) − f(…xᵢ−h…)) / 2h   (point is a list, i is the variable index)"""
    return (f(*[p + h if j == i else p for j, p in enumerate(point)]) - f(*[p - h if j == i else p for j, p in enumerate(point)])) / (2 * h)
