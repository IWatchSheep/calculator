"""Not element of   [∉]

Category : Math > Logic and sets
Formula  : x ∉ S  — x is not a member of S

Status   : ready to use - call compute(x, s)
"""

NAME = 'Not element of'
SYMBOL = '∉'
CATEGORY = 'Math'
SUBCATEGORY = 'Logic and sets'
FORMULA = 'x ∉ S  — x is not a member of S'


def compute(x, s):
    """x ∉ S  — x is not a member of S"""
    return x not in s
