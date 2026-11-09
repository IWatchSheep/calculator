"""Quadratic formula   [ax²+bx+c=0]

Category : Math > Algebra
Formula  : x = (−b ± √(b² − 4ac)) / 2a

Status   : ready to use - call compute(a, b, c)
"""
import cmath

NAME = 'Quadratic formula'
SYMBOL = 'ax²+bx+c=0'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = 'x = (−b ± √(b² − 4ac)) / 2a'


def compute(a, b, c):
    """x = (−b ± √(b² − 4ac)) / 2a"""
    return ((-b + cmath.sqrt(b * b - 4 * a * c)) / (2 * a), (-b - cmath.sqrt(b * b - 4 * a * c)) / (2 * a))
