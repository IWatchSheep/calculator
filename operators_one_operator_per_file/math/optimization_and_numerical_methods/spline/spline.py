"""Spline   [S(x)]

Category : Math > Optimization and numerical methods
Formula  : A piecewise polynomial (often cubic) joined smoothly at knots

Status   : ready to use - call compute(xs, ys, x)
"""

NAME = 'Spline'
SYMBOL = 'S(x)'
CATEGORY = 'Math'
SUBCATEGORY = 'Optimization and numerical methods'
FORMULA = 'A piecewise polynomial (often cubic) joined smoothly at knots'
import math
from operators_one_operator_per_file import _helpers as H


def compute(xs, ys, x):
    """Natural cubic spline through the points (xs, ys), evaluated at x"""
    n = len(xs)
    if n < 3 or sorted(xs) != list(xs):
        raise ValueError("give at least 3 increasing x values")
    h = [xs[i + 1] - xs[i] for i in range(n - 1)]
    A = [[0.0] * n for _ in range(n)]
    r = [0.0] * n
    A[0][0] = A[-1][-1] = 1.0
    for i in range(1, n - 1):
        A[i][i - 1], A[i][i], A[i][i + 1] = h[i - 1], 2 * (h[i - 1] + h[i]), h[i]
        r[i] = 3 * ((ys[i + 1] - ys[i]) / h[i] - (ys[i] - ys[i - 1]) / h[i - 1])
    R, _p = H.rref([A[i] + [r[i]] for i in range(n)])
    c = [R[i][n] for i in range(n)]
    if not xs[0] <= x <= xs[-1]:
        raise ValueError("x is outside the data")
    i = max(k for k in range(n - 1) if xs[k] <= x)
    dx = x - xs[i]
    b = (ys[i + 1] - ys[i]) / h[i] - h[i] * (2 * c[i] + c[i + 1]) / 3
    d = (c[i + 1] - c[i]) / (3 * h[i])
    return ys[i] + b * dx + c[i] * dx ** 2 + d * dx ** 3
