"""Range   [range]

Category : Math > Statistics and probability
Formula  : range = max − min

Status   : ready to use - call compute(data)
"""

NAME = 'Range'
SYMBOL = 'range'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'range = max − min'


def compute(data):
    """range = max − min"""
    return max(data) - min(data)
