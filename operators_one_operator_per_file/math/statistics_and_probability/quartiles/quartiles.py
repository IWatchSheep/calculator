"""Quartiles   [Q1 Q2 Q3]

Category : Math > Statistics and probability
Formula  : values that split sorted data into four equal parts

Status   : ready to use - call compute(data)
"""
import statistics

NAME = 'Quartiles'
SYMBOL = 'Q1 Q2 Q3'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'values that split sorted data into four equal parts'


def compute(data):
    """values that split sorted data into four equal parts"""
    return statistics.quantiles(data, n=4)
