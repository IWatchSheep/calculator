"""Percentile   [Pₖ]

Category : Math > Statistics and probability
Formula  : value below which k percent of the data fall (k = 1 … 99)

Status   : ready to use - call compute(data, k)
"""
import statistics

NAME = 'Percentile'
SYMBOL = 'Pₖ'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'value below which k percent of the data fall (k = 1 … 99)'


def compute(data, k):
    """value below which k percent of the data fall (k = 1 … 99)"""
    return statistics.quantiles(data, n=100)[k - 1]
