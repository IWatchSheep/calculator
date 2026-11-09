"""Injective   [one-to-one]

Category : Math > Category theory and foundations
Formula  : f(x) = f(y) ⇒ x = y

Status   : ready to use - call compute(f, domain)
"""

NAME = 'Injective'
SYMBOL = 'one-to-one'
CATEGORY = 'Math'
SUBCATEGORY = 'Category theory and foundations'
FORMULA = 'f(x) = f(y) ⇒ x = y'


def compute(f, domain):
    """f(x) = f(y) ⇒ x = y"""
    return len({f(x) for x in domain}) == len(list(domain))
