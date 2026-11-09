"""Mean   [x̄]

Category : Math > Statistics and probability
Formula  : mean = Σxᵢ / n

Status   : ready to use - call compute(data)
"""
import statistics

NAME = 'Mean'
SYMBOL = 'x̄'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'mean = Σxᵢ / n'


def compute(data):
    """mean = Σxᵢ / n"""
    return statistics.mean(data)
