"""Modulo   [%]

Category : Math > Arithmetic
Formula  : a mod b = a − b·⌊a/b⌋  (remainder of a ÷ b)

Status   : ready to use - call compute(a, b)
"""

NAME = 'Modulo'
SYMBOL = '%'
CATEGORY = 'Math'
SUBCATEGORY = 'Arithmetic'
FORMULA = 'a mod b = a − b·⌊a/b⌋  (remainder of a ÷ b)'


def compute(a, b):
    """a mod b = a − b·⌊a/b⌋  (remainder of a ÷ b)"""
    return a % b
