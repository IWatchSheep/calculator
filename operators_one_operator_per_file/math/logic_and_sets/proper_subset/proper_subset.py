"""Proper subset   [⊂]

Category : Math > Logic and sets
Formula  : A ⊂ B  — every element of A is in B and A ≠ B

Status   : ready to use - call compute(a, b)
"""

NAME = 'Proper subset'
SYMBOL = '⊂'
CATEGORY = 'Math'
SUBCATEGORY = 'Logic and sets'
FORMULA = 'A ⊂ B  — every element of A is in B and A ≠ B'


def compute(a, b):
    """A ⊂ B  — every element of A is in B and A ≠ B"""
    return set(a) < set(b)
