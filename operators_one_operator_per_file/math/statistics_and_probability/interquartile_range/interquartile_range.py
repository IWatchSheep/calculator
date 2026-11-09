"""Interquartile range   [IQR]

Category : Math > Statistics and probability
Formula  : IQR = Q3 − Q1

Status   : ready to use - call compute(data)
"""
import statistics

NAME = 'Interquartile range'
SYMBOL = 'IQR'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'IQR = Q3 − Q1'


def compute(data):
    """IQR = Q3 − Q1"""
    return statistics.quantiles(data, n=4)[2] - statistics.quantiles(data, n=4)[0]
