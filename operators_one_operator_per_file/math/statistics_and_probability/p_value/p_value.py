"""p-value   [p]

Category : Math > Statistics and probability
Formula  : probability, assuming the null hypothesis is true, of a result at least as extreme as the one observed

Status   : ready to use - call compute(z)
"""

NAME = 'p-value'
SYMBOL = 'p'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'probability, assuming the null hypothesis is true, of a result at least as extreme as the one observed'
import math
from operators_one_operator_per_file import _helpers as H


def compute(z):
    """Two-sided p-value for a z-score: 2·(1 − Φ(|z|))"""
    from statistics import NormalDist
    return 2 * (1 - NormalDist().cdf(abs(z)))
