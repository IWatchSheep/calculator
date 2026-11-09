"""Modulus of complex number   [|z|]

Category : Math > Algebra
Formula  : |a + bi| = √(a² + b²)

Status   : ready to use - call compute(z)
"""

NAME = 'Modulus of complex number'
SYMBOL = '|z|'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = '|a + bi| = √(a² + b²)'


def compute(z):
    """|a + bi| = √(a² + b²)"""
    return abs(z)
