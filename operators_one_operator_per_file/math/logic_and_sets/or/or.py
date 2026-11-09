"""OR   [∨]

Category : Math > Logic and sets
Formula  : A ∨ B is true when at least one is true

Status   : ready to use - call compute(a, b)
"""

NAME = 'OR'
SYMBOL = '∨'
CATEGORY = 'Math'
SUBCATEGORY = 'Logic and sets'
FORMULA = 'A ∨ B is true when at least one is true'


def compute(a, b):
    """A ∨ B is true when at least one is true"""
    return bool(a) or bool(b)
