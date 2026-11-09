"""Subset or equal   [⊆]

Category : Math > Logic and sets
Formula  : A ⊆ B  — every element of A is in B

Status   : ready to use - call compute(a, b)
"""

NAME = 'Subset or equal'
SYMBOL = '⊆'
CATEGORY = 'Math'
SUBCATEGORY = 'Logic and sets'
FORMULA = 'A ⊆ B  — every element of A is in B'


def compute(a, b):
    """A ⊆ B  — every element of A is in B"""
    return set(a) <= set(b)
