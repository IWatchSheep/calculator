"""Surjective   [onto]

Category : Math > Category theory and foundations
Formula  : every element of the codomain is f(x) for some x

Status   : ready to use - call compute(f, domain, codomain)
"""

NAME = 'Surjective'
SYMBOL = 'onto'
CATEGORY = 'Math'
SUBCATEGORY = 'Category theory and foundations'
FORMULA = 'every element of the codomain is f(x) for some x'


def compute(f, domain, codomain):
    """every element of the codomain is f(x) for some x"""
    return {f(x) for x in domain} == set(codomain)
