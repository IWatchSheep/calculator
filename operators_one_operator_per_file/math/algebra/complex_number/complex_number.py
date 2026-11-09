"""Complex number   [a + bi]

Category : Math > Algebra
Formula  : z = a + bi

Status   : ready to use - call compute(a, b)
"""

NAME = 'Complex number'
SYMBOL = 'a + bi'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = 'z = a + bi'


def compute(a, b):
    """z = a + bi"""
    return complex(a, b)
