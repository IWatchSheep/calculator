"""Slope-intercept form   [y = mx + b]

Category : Math > Algebra
Formula  : y = m·x + b

Status   : ready to use - call compute(m, x, b)
"""

NAME = 'Slope-intercept form'
SYMBOL = 'y = mx + b'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = 'y = m·x + b'


def compute(m, x, b):
    """y = m·x + b"""
    return m * x + b
