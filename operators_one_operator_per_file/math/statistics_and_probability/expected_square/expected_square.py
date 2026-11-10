"""Expected square   [E[X²]]

Category : Math > Statistics and probability
Formula  : E[X²] = Σ xᵢ² · pᵢ

Status   : ready to use - call compute(values, probs)
"""

NAME = 'Expected square'
SYMBOL = 'E[X²]'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'E[X²] = Σ xᵢ² · pᵢ'


def compute(values, probs):
    """E[X²] = Σ xᵢ² · pᵢ"""
    return sum(x * x * p for x, p in zip(values, probs))
