"""Contour integral   [∮ f(z) dz]

Category : Math > Complex analysis
Formula  : ∮_C f(z) dz = ∫ f(γ(t)) γ′(t) dt

Status   : ready to use - call compute(f, center, radius)
"""

NAME = 'Contour integral'
SYMBOL = '∮ f(z) dz'
CATEGORY = 'Math'
SUBCATEGORY = 'Complex analysis'
FORMULA = '∮_C f(z) dz = ∫ f(γ(t)) γ′(t) dt'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, center, radius):
    """∮ f(z) dz once round the circle |z − center| = radius (counter-clockwise); f uses z"""
    return H.circle_integral(f, center, radius)
