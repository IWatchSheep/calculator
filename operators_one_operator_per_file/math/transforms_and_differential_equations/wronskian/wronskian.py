"""Wronskian   [W(f, g)]

Category : Math > Transforms and differential equations
Formula  : W(f, g) = f·g′ − g·f′   (f, g and their derivatives at a point)

Status   : ready to use - call compute(f, fprime, g, gprime)
"""

NAME = 'Wronskian'
SYMBOL = 'W(f, g)'
CATEGORY = 'Math'
SUBCATEGORY = 'Transforms and differential equations'
FORMULA = 'W(f, g) = f·g′ − g·f′   (f, g and their derivatives at a point)'


def compute(f, fprime, g, gprime):
    """W(f, g) = f·g′ − g·f′   (f, g and their derivatives at a point)"""
    return f * gprime - g * fprime
