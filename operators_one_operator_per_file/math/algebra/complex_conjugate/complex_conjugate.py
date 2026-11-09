"""Complex conjugate   [z̄]

Category : Math > Algebra
Formula  : conj(a + bi) = a − bi

Status   : ready to use - call compute(z)
"""

NAME = 'Complex conjugate'
SYMBOL = 'z̄'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = 'conj(a + bi) = a − bi'


def compute(z):
    """conj(a + bi) = a − bi"""
    return complex(z).conjugate()
