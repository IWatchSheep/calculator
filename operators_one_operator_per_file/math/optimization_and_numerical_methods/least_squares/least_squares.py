"""Least squares   [min Σ(yᵢ − ŷᵢ)²]

Category : Math > Optimization and numerical methods
Formula  : Best-fit line y = mx + b minimizing squared error; returns (slope, intercept)

Status   : ready to use - call compute(x, y)
"""
import statistics

NAME = 'Least squares'
SYMBOL = 'min Σ(yᵢ − ŷᵢ)²'
CATEGORY = 'Math'
SUBCATEGORY = 'Optimization and numerical methods'
FORMULA = 'Best-fit line y = mx + b minimizing squared error; returns (slope, intercept)'


def compute(x, y):
    """Best-fit line y = mx + b minimizing squared error; returns (slope, intercept)"""
    return statistics.linear_regression(x, y)
