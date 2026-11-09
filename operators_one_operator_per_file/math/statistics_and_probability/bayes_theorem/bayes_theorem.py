"""Bayes' theorem   [P(A|B)]

Category : Math > Statistics and probability
Formula  : P(A|B) = P(B|A) · P(A) / P(B)

Status   : ready to use - call compute(p_b_given_a, p_a, p_b)
"""

NAME = "Bayes' theorem"
SYMBOL = 'P(A|B)'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'P(A|B) = P(B|A) · P(A) / P(B)'


def compute(p_b_given_a, p_a, p_b):
    """P(A|B) = P(B|A) · P(A) / P(B)"""
    return p_b_given_a * p_a / p_b
