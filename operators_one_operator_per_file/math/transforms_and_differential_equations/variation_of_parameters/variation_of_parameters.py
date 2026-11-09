"""Variation of parameters   [yₚ]

Category : Math > Transforms and differential equations
Formula  : Particular solution yₚ = −y₁∫(y₂ g / W) dx + y₂∫(y₁ g / W) dx

Status   : ready to use - call compute(y1, y2, g, x0, x)
"""

NAME = 'Variation of parameters'
SYMBOL = 'yₚ'
CATEGORY = 'Math'
SUBCATEGORY = 'Transforms and differential equations'
FORMULA = 'Particular solution yₚ = −y₁∫(y₂ g / W) dx + y₂∫(y₁ g / W) dx'
import math
from operators_one_operator_per_file import _helpers as H


def compute(y1, y2, g, x0, x):
    """Particular solution of y″ + p·y′ + q·y = g from two solutions y1, y2 of the plain equation:
    yₚ = −y1∫(y2·g/W) + y2∫(y1·g/W), W = y1·y2′ − y1′·y2   (integrals from x0 to x)"""
    def d(F, t, h=1e-5):
        return (F(t + h) - F(t - h)) / (2 * h)
    W = lambda t: y1(t) * d(y2, t) - d(y1, t) * y2(t)
    i1 = H.simpson(lambda t: y2(t) * g(t) / W(t), x0, x, 1000)
    i2 = H.simpson(lambda t: y1(t) * g(t) / W(t), x0, x, 1000)
    return -y1(x) * i1 + y2(x) * i2
