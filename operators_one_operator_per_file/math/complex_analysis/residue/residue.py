"""Residue   [Res(f, a)]

Category : Math > Complex analysis
Formula  : The coefficient of 1/(z − a) in the Laurent series of f about a

Status   : ready to use - call compute(f, a, radius=0.01)
"""

NAME = 'Residue'
SYMBOL = 'Res(f, a)'
CATEGORY = 'Math'
SUBCATEGORY = 'Complex analysis'
FORMULA = 'The coefficient of 1/(z − a) in the Laurent series of f about a'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, a, radius=0.01):
    """Res(f, a) = (1/2πi) ∮ f(z) dz on a small circle round the pole a; f uses z"""
    return H.circle_integral(f, a, radius) / (2j * math.pi)
