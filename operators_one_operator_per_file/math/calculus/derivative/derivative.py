"""Derivative   [d/dx]

Category : Math > Calculus
Formula  : f′(x) = lim_{h→0} (f(x+h) − f(x−h)) / 2h   (numerical central difference)

Status   : ready to use - call compute(f, x, h=1e-6)
"""

NAME = 'Derivative'
SYMBOL = 'd/dx'
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = 'f′(x) = lim_{h→0} (f(x+h) − f(x−h)) / 2h   (numerical central difference)'


def compute(f, x, h=1e-6):
    """f′(x) = lim_{h→0} (f(x+h) − f(x−h)) / 2h   (numerical central difference)"""
    return (f(x + h) - f(x - h)) / (2 * h)
