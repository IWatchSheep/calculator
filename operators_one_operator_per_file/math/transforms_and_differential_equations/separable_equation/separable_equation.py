"""Separable equation   [dy/dx = g(x)h(y)]

Category : Math > Transforms and differential equations
Formula  : Rewrite as dy/h(y) = g(x) dx and integrate both sides

Status   : ready to use - call compute(g, h, x0, y0, x_end)
"""

NAME = 'Separable equation'
SYMBOL = 'dy/dx = g(x)h(y)'
CATEGORY = 'Math'
SUBCATEGORY = 'Transforms and differential equations'
FORMULA = 'Rewrite as dy/h(y) = g(x) dx and integrate both sides'
import math
from operators_one_operator_per_file import _helpers as H


def compute(g, h, x0, y0, x_end):
    """Solve dy/dx = g(x)·h(y) from (x0, y0) to x_end.  Type g with x, and h with x as its variable too (it is applied to y)"""
    return H.rk4(lambda x, y: g(x) * h(y), x0, y0, x_end)
