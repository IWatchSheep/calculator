"""Interquartile range: from the quartiles   [IQR = Q3 − Q1]

Category : Math > Statistics and probability
Formula  : IQR = Q3 − Q1   (Q3 is the answer of Row 1, Q1 the answer of Row 2)

Status   : ready to use - call compute(q3, q1)
"""

NAME = 'Interquartile range: from the quartiles'
SYMBOL = 'IQR = Q3 − Q1'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'IQR = Q3 − Q1   (Q3 is the answer of Row 1, Q1 the answer of Row 2)'


def compute(q3, q1):
    """IQR = Q3 − Q1"""
    return q3 - q1
