"""Correlation   [r]

Category : Math > Statistics and probability
Formula  : r = cov(X,Y) / (sₓ · s_y)

Status   : ready to use - call compute(x, y)
"""
import statistics

NAME = 'Correlation'
SYMBOL = 'r'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'r = cov(X,Y) / (sₓ · s_y)'


def compute(x, y):
    """r = cov(X,Y) / (sₓ · s_y)"""
    return statistics.correlation(x, y)
