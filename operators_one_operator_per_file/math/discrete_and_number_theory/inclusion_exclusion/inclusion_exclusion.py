"""Inclusion-exclusion   [|A∪B|]

Category : Math > Discrete and number theory
Formula  : |A ∪ B| = |A| + |B| − |A ∩ B|

Status   : ready to use - call compute(a, b, a_and_b)
"""

NAME = 'Inclusion-exclusion'
SYMBOL = '|A∪B|'
CATEGORY = 'Math'
SUBCATEGORY = 'Discrete and number theory'
FORMULA = '|A ∪ B| = |A| + |B| − |A ∩ B|'


def compute(a, b, a_and_b):
    """|A ∪ B| = |A| + |B| − |A ∩ B|"""
    return a + b - a_and_b
