"""Chain rule   [(f∘g)′]

Category : Math > Calculus
Formula  : (f∘g)′(x) = f′(g(x)) · g′(x)

Status   : ready to use - call compute(fprime_at_gx, gprime_at_x)
"""

NAME = 'Chain rule'
SYMBOL = '(f∘g)′'
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = '(f∘g)′(x) = f′(g(x)) · g′(x)'


def compute(fprime_at_gx, gprime_at_x):
    """(f∘g)′(x) = f′(g(x)) · g′(x)"""
    return fprime_at_gx * gprime_at_x
