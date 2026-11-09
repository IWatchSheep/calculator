"""Cardinality   [|A|]

Category : Math > Logic and sets
Formula  : |A| = number of elements in A

Status   : ready to use - call compute(a)
"""

NAME = 'Cardinality'
SYMBOL = '|A|'
CATEGORY = 'Math'
SUBCATEGORY = 'Logic and sets'
FORMULA = '|A| = number of elements in A'


def compute(a):
    """|A| = number of elements in A"""
    return len(set(a))
