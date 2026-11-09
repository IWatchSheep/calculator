"""NOT   [¬]

Category : Math > Logic and sets
Formula  : ¬A is true when A is false

Status   : ready to use - call compute(a)
"""

NAME = 'NOT'
SYMBOL = '¬'
CATEGORY = 'Math'
SUBCATEGORY = 'Logic and sets'
FORMULA = '¬A is true when A is false'


def compute(a):
    """¬A is true when A is false"""
    return not a
