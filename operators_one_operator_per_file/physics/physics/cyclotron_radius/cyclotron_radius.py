"""Cyclotron radius of a charged particle   [r = mv/(|q|B)]

Category : Physics > Physics
Formula  : r = m v / (|q| B)   (charge moving perpendicular to B)

Status   : ready to use - call compute(m, v, q, B)
"""
import math

NAME = 'Cyclotron radius of a charged particle'
SYMBOL = 'r = mv/(|q|B)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'r = m v / (|q| B)   (charge moving perpendicular to B)'


def compute(m, v, q, B):
    """r = m v / (|q| B)   (charge moving perpendicular to B)"""
    return m * v / (abs(q) * B)
