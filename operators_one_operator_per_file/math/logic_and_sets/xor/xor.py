"""XOR   [⊕]

Category : Math > Logic and sets
Formula  : A ⊕ B is true when exactly one is true

Status   : ready to use - call compute(a, b)
"""

NAME = 'XOR'
SYMBOL = '⊕'
CATEGORY = 'Math'
SUBCATEGORY = 'Logic and sets'
FORMULA = 'A ⊕ B is true when exactly one is true'


def compute(a, b):
    """A ⊕ B is true when exactly one is true"""
    return bool(a) != bool(b)
