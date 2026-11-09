"""Mode   [mode]

Category : Math > Statistics and probability
Formula  : most frequent value

Status   : ready to use - call compute(data)
"""
import statistics

NAME = 'Mode'
SYMBOL = 'mode'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'most frequent value'


def compute(data):
    """most frequent value"""
    return statistics.mode(data)
