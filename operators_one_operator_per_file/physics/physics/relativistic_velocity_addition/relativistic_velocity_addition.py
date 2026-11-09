"""Relativistic velocity addition   [u′ = (u + v)/(1 + uv/c²)]

Category : Physics > Physics
Formula  : w = (u + v) / (1 + u v / c²)

Status   : ready to use - call compute(u, v, c)
"""
import math

NAME = 'Relativistic velocity addition'
SYMBOL = 'u′ = (u + v)/(1 + uv/c²)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'w = (u + v) / (1 + u v / c²)'


def compute(u, v, c=299792458):
    """w = (u + v) / (1 + u v / c²)"""
    return (u + v) / (1 + u * v / c ** 2)
