"""Linear regression   [y = mx + b]

Category : Math > Statistics and probability
Formula  : least-squares line; returns (slope, intercept)

Status   : ready to use - call compute(x, y)
"""
import statistics

NAME = 'Linear regression'
SYMBOL = 'y = mx + b'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'least-squares line; returns (slope, intercept)'


def compute(x, y):
    """least-squares line; returns (slope, intercept)"""
    return statistics.linear_regression(x, y)
