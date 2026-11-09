"""Brewster's angle   [θB = arctan(n₂/n₁)]

Category : Physics > Physics
Formula  : θB = arctan(n₂ / n₁)   (angle in radians)

Status   : ready to use - call compute(n1, n2)
"""
import math

NAME = "Brewster's angle"
SYMBOL = 'θB = arctan(n₂/n₁)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'θB = arctan(n₂ / n₁)   (angle in radians)'


def compute(n1, n2):
    """θB = arctan(n₂ / n₁)   (angle in radians)"""
    return math.atan(n2 / n1)
