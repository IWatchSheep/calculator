"""Third quartile   [Q3]

Category : Math > Statistics and probability
Formula  : Q3, the 75th percentile (quantiles of the list in four parts, the third cut)

Status   : ready to use - call compute(data)
"""
import statistics

NAME = 'Third quartile'
SYMBOL = 'Q3'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'Q3, the 75th percentile (quantiles of the list in four parts, the third cut)'


def compute(data):
    """Q3 = quantiles(data, n=4)[2]"""
    return statistics.quantiles(data, n=4)[2]
