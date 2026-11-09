"""Absolute value   [|x|]

Category : Math > Arithmetic
Formula  : |x| = x if x ≥ 0, otherwise −x

Status   : ready to use - call compute(x)
"""

NAME = 'Absolute value'
SYMBOL = '|x|'
CATEGORY = 'Math'
SUBCATEGORY = 'Arithmetic'
FORMULA = '|x| = x if x ≥ 0, otherwise −x'


def compute(x):
    """|x| = x if x ≥ 0, otherwise −x"""
    return abs(x)
