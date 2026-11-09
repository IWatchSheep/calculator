"""First-order ODE   [y′ = f(x, y)]

Category : Math > Transforms and differential equations
Formula  : An ordinary differential equation involving only the first derivative

Status   : ready to use - call compute(f, x0, y0, x_end)
"""

NAME = 'First-order ODE'
SYMBOL = 'y′ = f(x, y)'
CATEGORY = 'Math'
SUBCATEGORY = 'Transforms and differential equations'
FORMULA = 'An ordinary differential equation involving only the first derivative'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, x0, y0, x_end):
    """Solve y′ = f(x, y) from (x0, y0) to x_end  (Runge–Kutta 4)"""
    return H.rk4(f, x0, y0, x_end)
