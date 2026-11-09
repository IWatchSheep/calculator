"""Cartesian product   [A × B]

Category : Math > Category theory and foundations
Formula  : A × B = { (a, b) : a ∈ A, b ∈ B }

Status   : ready to use - call compute(a, b)
"""
import itertools

NAME = 'Cartesian product'
SYMBOL = 'A × B'
CATEGORY = 'Math'
SUBCATEGORY = 'Category theory and foundations'
FORMULA = 'A × B = { (a, b) : a ∈ A, b ∈ B }'


def compute(a, b):
    """A × B = { (a, b) : a ∈ A, b ∈ B }"""
    return list(itertools.product(a, b))
