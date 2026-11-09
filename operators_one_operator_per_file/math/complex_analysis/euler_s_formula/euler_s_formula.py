"""Euler's formula   [e^(iθ)]

Category : Math > Complex analysis
Formula  : e^(iθ) = cos θ + i sin θ

Status   : ready to use - call compute(theta)
"""
import cmath

NAME = "Euler's formula"
SYMBOL = 'e^(iθ)'
CATEGORY = 'Math'
SUBCATEGORY = 'Complex analysis'
FORMULA = 'e^(iθ) = cos θ + i sin θ'


def compute(theta):
    """e^(iθ) = cos θ + i sin θ"""
    return cmath.exp(1j * theta)
