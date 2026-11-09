"""If and only if   [↔]

Category : Math > Logic and sets
Formula  : A ↔ B is true when A and B have the same truth value

Status   : ready to use - call compute(a, b)
"""

NAME = 'If and only if'
SYMBOL = '↔'
CATEGORY = 'Math'
SUBCATEGORY = 'Logic and sets'
FORMULA = 'A ↔ B is true when A and B have the same truth value'


def compute(a, b):
    """A ↔ B is true when A and B have the same truth value"""
    return bool(a) == bool(b)
