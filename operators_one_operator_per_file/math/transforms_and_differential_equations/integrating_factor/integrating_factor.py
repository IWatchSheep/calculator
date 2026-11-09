"""Integrating factor   [μ(x)]

Category : Math > Transforms and differential equations
Formula  : For y′ + P(x)y = Q(x):  μ = e^(∫P dx),  (μy)′ = μQ

Status   : ready to use - call compute(P, x0, x)
"""

NAME = 'Integrating factor'
SYMBOL = 'μ(x)'
CATEGORY = 'Math'
SUBCATEGORY = 'Transforms and differential equations'
FORMULA = 'For y′ + P(x)y = Q(x):  μ = e^(∫P dx),  (μy)′ = μQ'
import math
from operators_one_operator_per_file import _helpers as H


def compute(P, x0, x):
    """μ(x) = e^(∫P dx), with the integral taken from x0 to x"""
    return math.exp(H.simpson(P, x0, x, 1000))
