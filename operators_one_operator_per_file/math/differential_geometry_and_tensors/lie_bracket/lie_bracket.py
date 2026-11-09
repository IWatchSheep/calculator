"""Lie bracket   [[X, Y]]

Category : Math > Differential geometry and tensors
Formula  : [X, Y] f = X(Y f) − Y(X f)

Status   : ready to use - call compute(X, Y, point)
"""

NAME = 'Lie bracket'
SYMBOL = '[X, Y]'
CATEGORY = 'Math'
SUBCATEGORY = 'Differential geometry and tensors'
FORMULA = '[X, Y] f = X(Y f) − Y(X f)'
import math
from operators_one_operator_per_file import _helpers as H


def compute(X, Y, point):
    """[X, Y] at a point: Σⱼ (Xʲ ∂ⱼYⁱ − Yʲ ∂ⱼXⁱ)  (X and Y each give a list)"""
    n = len(point)
    Xp, Yp = X(*point), Y(*point)
    out = []
    for i in range(n):
        s = 0.0
        for j in range(n):
            s += Xp[j] * H.partial(lambda *p: Y(*p)[i], point, j) - Yp[j] * H.partial(lambda *p: X(*p)[i], point, j)
        out.append(s)
    return out
