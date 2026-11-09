"""Curl   [∇×]

Category : Math > Calculus
Formula  : ∇×F = (∂Fz/∂y − ∂Fy/∂z, ∂Fx/∂z − ∂Fz/∂x, ∂Fy/∂x − ∂Fx/∂y)

Status   : ready to use - call compute(F, point)
"""

NAME = 'Curl'
SYMBOL = '∇×'
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = '∇×F = (∂Fz/∂y − ∂Fy/∂z, ∂Fx/∂z − ∂Fz/∂x, ∂Fy/∂x − ∂Fx/∂y)'
import math
from operators_one_operator_per_file import _helpers as H


def compute(F, point):
    """∇×F at a 3-D point  (F gives a list of 3 components)"""
    if len(point) != 3:
        raise ValueError("curl needs a 3-D point")
    d = lambda comp, var: H.partial(lambda *p: F(*p)[comp], point, var)
    return [d(2, 1) - d(1, 2), d(0, 2) - d(2, 0), d(1, 0) - d(0, 1)]
