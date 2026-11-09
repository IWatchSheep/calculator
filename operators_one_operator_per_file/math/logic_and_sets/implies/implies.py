"""Implies   [→]

Category : Math > Logic and sets
Formula  : A → B is false only when A is true and B is false  (¬A ∨ B)

Status   : ready to use - call compute(a, b)
"""

NAME = 'Implies'
SYMBOL = '→'
CATEGORY = 'Math'
SUBCATEGORY = 'Logic and sets'
FORMULA = 'A → B is false only when A is true and B is false  (¬A ∨ B)'


def compute(a, b):
    """A → B is false only when A is true and B is false  (¬A ∨ B)"""
    return (not a) or bool(b)
