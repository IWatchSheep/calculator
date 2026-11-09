"""Heaviside step   [H(x)]

Category : Math > Transforms and differential equations
Formula  : H(x) = 0 for x < 0, 1 for x > 0 (½ at 0)

Status   : ready to use - call compute(x)
"""

NAME = 'Heaviside step'
SYMBOL = 'H(x)'
CATEGORY = 'Math'
SUBCATEGORY = 'Transforms and differential equations'
FORMULA = 'H(x) = 0 for x < 0, 1 for x > 0 (½ at 0)'


def compute(x):
    """H(x) = 0 for x < 0, 1 for x > 0 (½ at 0)"""
    return 1.0 if x > 0 else (0.0 if x < 0 else 0.5)
