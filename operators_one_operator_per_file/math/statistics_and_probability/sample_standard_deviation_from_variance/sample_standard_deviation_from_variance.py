"""Sample standard deviation: from the sample variance   [s = √(s²)]

Category : Math > Statistics and probability
Formula  : s = √(s²)   (s² is the answer of the row above)

Status   : ready to use - call compute(sample_variance)
"""
import math

NAME = 'Sample standard deviation: from the sample variance'
SYMBOL = 's = √(s²)'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 's = √(s²)   (s² is the answer of the row above)'


def compute(sample_variance):
    """s = √(s²)"""
    return math.sqrt(sample_variance)
