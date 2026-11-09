"""Cauchy–Riemann equations   [uₓ = v_y]

Category : Math > Complex analysis
Formula  : f = u + iv is complex-differentiable only if ∂u/∂x = ∂v/∂y and ∂u/∂y = −∂v/∂x

Status   : ready to use - call compute(u, v, x0, y0)
"""

NAME = 'Cauchy–Riemann equations'
SYMBOL = 'uₓ = v_y'
CATEGORY = 'Math'
SUBCATEGORY = 'Complex analysis'
FORMULA = 'f = u + iv is complex-differentiable only if ∂u/∂x = ∂v/∂y and ∂u/∂y = −∂v/∂x'
import math
from operators_one_operator_per_file import _helpers as H


def compute(u, v, x0, y0):
    """Checks ∂u/∂x = ∂v/∂y and ∂u/∂y = −∂v/∂x at (x0, y0)  → (True/False, the two differences)"""
    p = [x0, y0]
    e1 = H.partial(u, p, 0) - H.partial(v, p, 1)
    e2 = H.partial(u, p, 1) + H.partial(v, p, 0)
    return (abs(e1) < 1e-4 and abs(e2) < 1e-4), e1, e2
