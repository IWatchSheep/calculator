"""AND   [∧]

Category : Math > Logic and sets
Formula  : A ∧ B is true only when both are true

Status   : ready to use - call compute(a, b)
"""

NAME = 'AND'
SYMBOL = '∧'
CATEGORY = 'Math'
SUBCATEGORY = 'Logic and sets'
FORMULA = 'A ∧ B is true only when both are true'


def compute(a, b):
    """A ∧ B is true only when both are true"""
    return bool(a) and bool(b)
