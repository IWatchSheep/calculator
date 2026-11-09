"""Second partial derivative   [∂²/∂x²]

Category : Math > Calculus
Formula  : ∂²f/∂xᵢ² ≈ (f(…xᵢ+h…) − 2f(…) + f(…xᵢ−h…)) / h²   (point is a list, i is the variable index)

Status   : ready to use - call compute(f, point, i, h=0.001)
"""

NAME = 'Second partial derivative'
SYMBOL = '∂²/∂x²'
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = '∂²f/∂xᵢ² ≈ (f(…xᵢ+h…) − 2f(…) + f(…xᵢ−h…)) / h²   (point is a list, i is the variable index)'


def compute(f, point, i, h=1e-3):
    """∂²f/∂xᵢ² ≈ (f(…xᵢ+h…) − 2f(…) + f(…xᵢ−h…)) / h²   (point is a list, i is the variable index)"""
    up = f(*[p + h if j == i else p for j, p in enumerate(point)])
    mid = f(*point)
    down = f(*[p - h if j == i else p for j, p in enumerate(point)])
    return (up - 2 * mid + down) / (h * h)
