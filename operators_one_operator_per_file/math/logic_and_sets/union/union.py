"""Union   [∪]

Category : Math > Logic and sets
Formula  : A ∪ B = elements in A or B (or both)

Status   : ready to use - call compute(a, b)
"""

NAME = 'Union'
SYMBOL = '∪'
CATEGORY = 'Math'
SUBCATEGORY = 'Logic and sets'
FORMULA = 'A ∪ B = elements in A or B (or both)'


def compute(a, b):
    """A ∪ B = elements in A or B (or both)"""
    return set(a) | set(b)
