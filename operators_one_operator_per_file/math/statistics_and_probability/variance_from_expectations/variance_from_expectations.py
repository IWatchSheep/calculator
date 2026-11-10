"""Variance: from the expectations   [Var = E[X²] − (E[X])²]

Category : Math > Statistics and probability
Formula  : Var = E[X²] − (E[X])²   (E[X²] is the answer of Row 2, E[X] the answer of Row 1)

Status   : ready to use - call compute(ex2, ex)
"""

NAME = 'Variance: from the expectations'
SYMBOL = 'Var = E[X²] − (E[X])²'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'Var = E[X²] − (E[X])²   (E[X²] is the answer of Row 2, E[X] the answer of Row 1)'


def compute(ex2, ex):
    """Var = E[X²] − (E[X])²"""
    return ex2 - ex ** 2
