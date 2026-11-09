"""Element of   [∈]

Category : Math > Logic and sets
Formula  : x ∈ S  — x is a member of S

Status   : ready to use - call compute(x, s)
"""

NAME = 'Element of'
SYMBOL = '∈'
CATEGORY = 'Math'
SUBCATEGORY = 'Logic and sets'
FORMULA = 'x ∈ S  — x is a member of S'


def compute(x, s):
    """x ∈ S  — x is a member of S"""
    return x in s
