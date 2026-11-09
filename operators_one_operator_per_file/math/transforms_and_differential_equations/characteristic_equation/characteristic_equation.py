"""Characteristic equation   [ar² + br + c = 0]

Category : Math > Transforms and differential equations
Formula  : For ay″ + by′ + cy = 0 try y = e^(rx) and solve the quadratic for r

Status   : ready to use - call compute(a, b, c)
"""

NAME = 'Characteristic equation'
SYMBOL = 'ar² + br + c = 0'
CATEGORY = 'Math'
SUBCATEGORY = 'Transforms and differential equations'
FORMULA = 'For ay″ + by′ + cy = 0 try y = e^(rx) and solve the quadratic for r'
import math
from operators_one_operator_per_file import _helpers as H


import cmath


def compute(a, b, c):
    """For a·y″ + b·y′ + c·y = 0: the two roots r of a·r² + b·r + c = 0 (solutions e^(r·x))"""
    d = cmath.sqrt(b * b - 4 * a * c)
    return (-b + d) / (2 * a), (-b - d) / (2 * a)
