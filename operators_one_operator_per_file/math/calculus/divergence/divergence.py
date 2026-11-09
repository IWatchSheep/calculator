"""Divergence   [∇·]

Category : Math > Calculus
Formula  : ∇·F = ∂Fx/∂x + ∂Fy/∂y + ∂Fz/∂z

Status   : ready to use - call compute(F, point)
"""

NAME = 'Divergence'
SYMBOL = '∇·'
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = '∇·F = ∂Fx/∂x + ∂Fy/∂y + ∂Fz/∂z'
import math
from operators_one_operator_per_file import _helpers as H


def compute(F, point):
    """∇·F = ∂Fx/∂x + ∂Fy/∂y + ∂Fz/∂z at a point  (F gives a list, e.g. [x*y, y*z, z*x])"""
    return sum(H.partial(lambda *p, i=i: F(*p)[i], point, i) for i in range(len(point)))
