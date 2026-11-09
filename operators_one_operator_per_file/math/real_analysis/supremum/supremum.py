"""Supremum   [sup]

Category : Math > Real analysis
Formula  : least upper bound of a set (for a finite set, the maximum)

Status   : ready to use - call compute(values)
"""

NAME = 'Supremum'
SYMBOL = 'sup'
CATEGORY = 'Math'
SUBCATEGORY = 'Real analysis'
FORMULA = 'least upper bound of a set (for a finite set, the maximum)'


def compute(values):
    """least upper bound of a set (for a finite set, the maximum)"""
    return max(values)
