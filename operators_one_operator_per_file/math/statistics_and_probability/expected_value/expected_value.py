"""Expected value   [E[X]]

Category : Math > Statistics and probability
Formula  : E[X] = Σ xᵢ · pᵢ

Status   : ready to use - call compute(values, probs)
"""

NAME = 'Expected value'
SYMBOL = 'E[X]'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'E[X] = Σ xᵢ · pᵢ'


def compute(values, probs):
    """E[X] = Σ xᵢ · pᵢ"""
    return sum(x * p for x, p in zip(values, probs))
