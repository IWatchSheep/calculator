"""Metric space distance   [d(x, y)]

Category : Math > Topology
Formula  : d(x, y) = √Σ(xᵢ − yᵢ)²   (Euclidean metric)

Status   : ready to use - call compute(x, y)
"""
import math

NAME = 'Metric space distance'
SYMBOL = 'd(x, y)'
CATEGORY = 'Math'
SUBCATEGORY = 'Topology'
FORMULA = 'd(x, y) = √Σ(xᵢ − yᵢ)²   (Euclidean metric)'


def compute(x, y):
    """d(x, y) = √Σ(xᵢ − yᵢ)²   (Euclidean metric)"""
    return math.dist(x, y)
