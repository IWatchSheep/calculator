"""For all   [∀]

Category : Math > Logic and sets
Formula  : ∀x ∈ D: P(x)  — P holds for every x in D

Status   : ready to use - call compute(predicate, domain)
"""

NAME = 'For all'
SYMBOL = '∀'
CATEGORY = 'Math'
SUBCATEGORY = 'Logic and sets'
FORMULA = '∀x ∈ D: P(x)  — P holds for every x in D'


def compute(predicate, domain):
    """∀x ∈ D: P(x)  — P holds for every x in D"""
    return all(predicate(x) for x in domain)
