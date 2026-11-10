"""Heron's formula: area   [√(s(s−a)(s−b)(s−c))]

Category : Geometry > Geometry
Formula  : A = √(s(s−a)(s−b)(s−c))   (s is the semi-perimeter, from the row above)

Status   : ready to use - call compute(s, a, b, c)
"""
import math

NAME = "Heron's formula: area"
SYMBOL = '√(s(s−a)(s−b)(s−c))'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'A = √(s(s−a)(s−b)(s−c))   (s is the semi-perimeter, from the row above)'


def compute(s, a, b, c):
    """A = √(s(s−a)(s−b)(s−c))"""
    return math.sqrt(s * (s - a) * (s - b) * (s - c))
