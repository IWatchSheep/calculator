"""Confidence interval   [CI]

Category : Math > Statistics and probability
Formula  : x̄ ± z · s / √n   (z = 1.96 for 95%)

Status   : ready to use - call compute(mean, sd, n, z=1.96)
"""
import math

NAME = 'Confidence interval'
SYMBOL = 'CI'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'x̄ ± z · s / √n   (z = 1.96 for 95%)'


def compute(mean, sd, n, z=1.96):
    """x̄ ± z · s / √n   (z = 1.96 for 95%)"""
    return (mean - z * sd / math.sqrt(n), mean + z * sd / math.sqrt(n))
