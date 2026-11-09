"""Quaternions   [ℍ]

Category : Math > Category theory and foundations
Formula  : { a + bi + cj + dk } with i² = j² = k² = ijk = −1

Status   : ready to use - call compute(a, b, c, d)
"""

NAME = 'Quaternions'
SYMBOL = 'ℍ'
CATEGORY = 'Math'
SUBCATEGORY = 'Category theory and foundations'
FORMULA = '{ a + bi + cj + dk } with i² = j² = k² = ijk = −1'
import math
from operators_one_operator_per_file import _helpers as H


def compute(a, b, c, d):
    """The size (norm) of the quaternion a + bi + cj + dk:  √(a² + b² + c² + d²)"""
    return math.sqrt(a * a + b * b + c * c + d * d)
