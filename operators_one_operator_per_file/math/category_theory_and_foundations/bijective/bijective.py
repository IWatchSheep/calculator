"""Bijective   [one-to-one and onto]

Category : Math > Category theory and foundations
Formula  : both injective and surjective

Status   : ready to use - call compute(f, domain, codomain)
"""

NAME = 'Bijective'
SYMBOL = 'one-to-one and onto'
CATEGORY = 'Math'
SUBCATEGORY = 'Category theory and foundations'
FORMULA = 'both injective and surjective'


def compute(f, domain, codomain):
    """both injective and surjective"""
    return len({f(x) for x in domain}) == len(list(domain)) and {f(x) for x in domain} == set(codomain)
