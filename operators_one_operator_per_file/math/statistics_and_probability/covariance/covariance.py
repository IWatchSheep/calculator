"""Covariance   [cov(X,Y)]

Category : Math > Statistics and probability
Formula  : cov(X,Y) = Σ(xᵢ − x̄)(yᵢ − ȳ) / (n − 1)

Status   : ready to use - call compute(x, y)
"""
import statistics

NAME = 'Covariance'
SYMBOL = 'cov(X,Y)'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'cov(X,Y) = Σ(xᵢ − x̄)(yᵢ − ȳ) / (n − 1)'


def compute(x, y):
    """cov(X,Y) = Σ(xᵢ − x̄)(yᵢ − ȳ) / (n − 1)"""
    return statistics.covariance(x, y)
