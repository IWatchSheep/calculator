"""Cauchy integral formula   [f(a)]

Category : Math > Complex analysis
Formula  : f(a) = (1 / 2πi) ∮ f(z) / (z − a) dz

Status   : ready to use - call compute(f, a, radius)
"""

NAME = 'Cauchy integral formula'
SYMBOL = 'f(a)'
CATEGORY = 'Math'
SUBCATEGORY = 'Complex analysis'
FORMULA = 'f(a) = (1 / 2πi) ∮ f(z) / (z − a) dz'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, a, radius):
    """f(a) = (1/2πi) ∮ f(z)/(z − a) dz  over a circle round a (f analytic inside); f uses z"""
    return H.circle_integral(lambda z: f(z) / (z - a), a, radius) / (2j * math.pi)
