"""Conditional probability   [P(A|B)]

Category : Math > Statistics and probability
Formula  : P(A|B) = P(A ∩ B) / P(B)

Status   : ready to use - call compute(p_a_and_b, p_b)
"""

NAME = 'Conditional probability'
SYMBOL = 'P(A|B)'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'P(A|B) = P(A ∩ B) / P(B)'


def compute(p_a_and_b, p_b):
    """P(A|B) = P(A ∩ B) / P(B)"""
    return p_a_and_b / p_b
