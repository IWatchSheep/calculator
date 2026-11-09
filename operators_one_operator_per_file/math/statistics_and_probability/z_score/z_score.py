"""Z-score   [z]

Category : Math > Statistics and probability
Formula  : z = (x − μ) / σ

Status   : ready to use - call compute(x, mean, sd)
"""

NAME = 'Z-score'
SYMBOL = 'z'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'z = (x − μ) / σ'


def compute(x, mean, sd):
    """z = (x − μ) / σ"""
    return (x - mean) / sd
