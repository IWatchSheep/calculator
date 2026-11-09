"""Quotient rule   [(f/g)′]

Category : Math > Calculus
Formula  : (f/g)′ = (f′g − fg′) / g²

Status   : ready to use - call compute(f, fprime, g, gprime)
"""

NAME = 'Quotient rule'
SYMBOL = '(f/g)′'
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = '(f/g)′ = (f′g − fg′) / g²'


def compute(f, fprime, g, gprime):
    """(f/g)′ = (f′g − fg′) / g²"""
    return (fprime * g - f * gprime) / g ** 2
