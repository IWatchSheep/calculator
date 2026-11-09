"""Complement   [Aᶜ]

Category : Math > Logic and sets
Formula  : Aᶜ = elements of the universal set U not in A

Status   : ready to use - call compute(a, universe)
"""

NAME = 'Complement'
SYMBOL = 'Aᶜ'
CATEGORY = 'Math'
SUBCATEGORY = 'Logic and sets'
FORMULA = 'Aᶜ = elements of the universal set U not in A'


def compute(a, universe):
    """Aᶜ = elements of the universal set U not in A"""
    return set(universe) - set(a)
