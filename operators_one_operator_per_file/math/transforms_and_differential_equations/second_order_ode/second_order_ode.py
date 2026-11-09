"""Second-order ODE   [y″ = f(x, y, y′)]

Category : Math > Transforms and differential equations
Formula  : An ordinary differential equation involving up to the second derivative

Status   : ready to use - call compute(f, x0, y0, v0, x_end)
"""

NAME = 'Second-order ODE'
SYMBOL = 'y″ = f(x, y, y′)'
CATEGORY = 'Math'
SUBCATEGORY = 'Transforms and differential equations'
FORMULA = 'An ordinary differential equation involving up to the second derivative'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, x0, y0, v0, x_end):
    """Solve y″ = f(x, y, y′) with y(x0) = y0, y′(x0) = v0, up to x_end → y(x_end).  In f use x, y and z (z = y′)"""
    sol = H.rk4(lambda x, s: [s[1], f(x, s[0], s[1])], x0, [y0, v0], x_end)
    return sol[0]
