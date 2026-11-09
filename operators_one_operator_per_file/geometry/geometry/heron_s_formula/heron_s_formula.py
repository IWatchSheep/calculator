"""Heron's formula   [√(s(s−a)(s−b)(s−c))]

Category : Geometry > Geometry
Formula  : A = √(s(s−a)(s−b)(s−c)),  s = (a + b + c)/2

Status   : ready to use - call compute(a, b, c)
"""
import math

NAME = "Heron's formula"
SYMBOL = '√(s(s−a)(s−b)(s−c))'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'A = √(s(s−a)(s−b)(s−c)),  s = (a + b + c)/2'


def compute(a, b, c):
    """A = √(s(s−a)(s−b)(s−c)),  s = (a + b + c)/2"""
    return math.sqrt((a + b + c) / 2 * ((a + b + c) / 2 - a) * ((a + b + c) / 2 - b) * ((a + b + c) / 2 - c))
