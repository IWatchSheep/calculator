"""Minimum   [min]

Category : Math > Arithmetic
Formula  : min(a, b, …) = smallest value

Status   : ready to use - call compute(*values)
"""

NAME = 'Minimum'
SYMBOL = 'min'
CATEGORY = 'Math'
SUBCATEGORY = 'Arithmetic'
FORMULA = 'min(a, b, …) = smallest value'


def compute(*values):
    """min(a, b, …) = smallest value"""
    return min(values)
