"""Set difference   [A − B]

Category : Math > Logic and sets
Formula  : A − B = elements of A that are not in B

Status   : ready to use - call compute(a, b)
"""

NAME = 'Set difference'
SYMBOL = 'A − B'
CATEGORY = 'Math'
SUBCATEGORY = 'Logic and sets'
FORMULA = 'A − B = elements of A that are not in B'


def compute(a, b):
    """A − B = elements of A that are not in B"""
    return set(a) - set(b)
