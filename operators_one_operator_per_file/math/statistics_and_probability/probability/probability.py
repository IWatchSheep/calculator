"""Probability   [P(A)]

Category : Math > Statistics and probability
Formula  : P(A) = favorable outcomes / total outcomes

Status   : ready to use - call compute(favorable, total)
"""

NAME = 'Probability'
SYMBOL = 'P(A)'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'P(A) = favorable outcomes / total outcomes'


def compute(favorable, total):
    """P(A) = favorable outcomes / total outcomes"""
    return favorable / total
