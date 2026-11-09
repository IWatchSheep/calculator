"""Intersection   [∩]

Category : Math > Logic and sets
Formula  : A ∩ B = elements in both A and B

Status   : ready to use - call compute(a, b)
"""

NAME = 'Intersection'
SYMBOL = '∩'
CATEGORY = 'Math'
SUBCATEGORY = 'Logic and sets'
FORMULA = 'A ∩ B = elements in both A and B'


def compute(a, b):
    """A ∩ B = elements in both A and B"""
    return set(a) & set(b)
