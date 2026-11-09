"""Mean value theorem   [f′(c)]

Category : Math > Real analysis
Formula  : f′(c) = (f(b) − f(a)) / (b − a) for some c in (a, b)

Status   : ready to use - call compute(f, a, b)
"""

NAME = 'Mean value theorem'
SYMBOL = 'f′(c)'
CATEGORY = 'Math'
SUBCATEGORY = 'Real analysis'
FORMULA = 'f′(c) = (f(b) − f(a)) / (b − a) for some c in (a, b)'


def compute(f, a, b):
    """f′(c) = (f(b) − f(a)) / (b − a) for some c in (a, b)"""
    return (f(b) - f(a)) / (b - a)
