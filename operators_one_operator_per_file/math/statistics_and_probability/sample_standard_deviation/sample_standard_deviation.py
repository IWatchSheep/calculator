"""Sample standard deviation   [s]

Category : Math > Statistics and probability
Formula  : s = √(s²)

Status   : ready to use - call compute(data)
"""
import statistics

NAME = 'Sample standard deviation'
SYMBOL = 's'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 's = √(s²)'


def compute(data):
    """s = √(s²)"""
    return statistics.stdev(data)
