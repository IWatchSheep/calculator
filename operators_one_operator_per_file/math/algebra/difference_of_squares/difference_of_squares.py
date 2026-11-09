"""Difference of squares   [a²−b²]

Category : Math > Algebra
Formula  : a² − b² = (a − b)(a + b)  (returns the two factors)

Status   : ready to use - call compute(a, b)
"""

NAME = 'Difference of squares'
SYMBOL = 'a²−b²'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = 'a² − b² = (a − b)(a + b)  (returns the two factors)'


def compute(a, b):
    """a² − b² = (a − b)(a + b)  (returns the two factors)"""
    return (a - b, a + b)
