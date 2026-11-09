"""Median   [median]

Category : Math > Statistics and probability
Formula  : middle value of the sorted data (average of the two middle values if n is even)

Status   : ready to use - call compute(data)
"""
import statistics

NAME = 'Median'
SYMBOL = 'median'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'middle value of the sorted data (average of the two middle values if n is even)'


def compute(data):
    """middle value of the sorted data (average of the two middle values if n is even)"""
    return statistics.median(data)
