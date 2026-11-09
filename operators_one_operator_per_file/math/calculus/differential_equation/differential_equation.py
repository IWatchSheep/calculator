"""Differential equation   [dy/dx = f(x,y)]

Category : Math > Calculus
Formula  : An equation relating a function to its derivatives; see the Euler / Runge–Kutta operators to solve numerically

Status   : ready to use - call compute(f, x0, y0, x_end)
"""

NAME = 'Differential equation'
SYMBOL = 'dy/dx = f(x,y)'
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = 'An equation relating a function to its derivatives; see the Euler / Runge–Kutta operators to solve numerically'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, x0, y0, x_end):
    """Solve y′ = f(x, y) from (x0, y0) to x = x_end  (Runge–Kutta 4)"""
    return H.rk4(f, x0, y0, x_end)
