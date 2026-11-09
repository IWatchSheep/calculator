"""Product rule   [(fg)′]

Category : Math > Calculus
Formula  : (f·g)′ = f′g + fg′

Status   : ready to use - call compute(f, fprime, g, gprime)
"""

NAME = 'Product rule'
SYMBOL = '(fg)′'
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = '(f·g)′ = f′g + fg′'


def compute(f, fprime, g, gprime):
    """(f·g)′ = f′g + fg′"""
    return fprime * g + f * gprime
