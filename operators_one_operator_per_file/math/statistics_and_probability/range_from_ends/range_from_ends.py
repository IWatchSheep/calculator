"""Range: from the ends   [range = max − min]

Category : Math > Statistics and probability
Formula  : range = max − min   (max is the answer of Row 1, min the answer of Row 2)

Status   : ready to use - call compute(maximum, minimum)
"""

NAME = 'Range: from the ends'
SYMBOL = 'range = max − min'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'range = max − min   (max is the answer of Row 1, min the answer of Row 2)'


def compute(maximum, minimum):
    """range = max − min"""
    return maximum - minimum
