"""First quartile   [Q1]

Category : Math > Statistics and probability
Formula  : Q1, the 25th percentile (quantiles of the list in four parts, the first cut)

Status   : ready to use - call compute(data)
"""
import statistics

NAME = 'First quartile'
SYMBOL = 'Q1'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'Q1, the 25th percentile (quantiles of the list in four parts, the first cut)'


def compute(data):
    """Q1 = quantiles(data, n=4)[0]"""
    return statistics.quantiles(data, n=4)[0]
