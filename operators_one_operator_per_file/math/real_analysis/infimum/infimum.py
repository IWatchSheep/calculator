"""Infimum   [inf]

Category : Math > Real analysis
Formula  : greatest lower bound of a set (for a finite set, the minimum)

Status   : ready to use - call compute(values)
"""

NAME = 'Infimum'
SYMBOL = 'inf'
CATEGORY = 'Math'
SUBCATEGORY = 'Real analysis'
FORMULA = 'greatest lower bound of a set (for a finite set, the minimum)'


def compute(values):
    """greatest lower bound of a set (for a finite set, the minimum)"""
    return min(values)
