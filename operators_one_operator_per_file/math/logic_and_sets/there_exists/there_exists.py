"""There exists   [∃]

Category : Math > Logic and sets
Formula  : ∃x ∈ D: P(x)  — P holds for at least one x in D

Status   : ready to use - call compute(predicate, domain)
"""

NAME = 'There exists'
SYMBOL = '∃'
CATEGORY = 'Math'
SUBCATEGORY = 'Logic and sets'
FORMULA = '∃x ∈ D: P(x)  — P holds for at least one x in D'


def compute(predicate, domain):
    """∃x ∈ D: P(x)  — P holds for at least one x in D"""
    return any(predicate(x) for x in domain)
