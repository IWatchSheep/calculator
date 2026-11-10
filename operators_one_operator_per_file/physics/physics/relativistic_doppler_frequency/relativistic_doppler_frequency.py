"""Relativistic Doppler: frequency   [f = f₀√((1−β)/(1+β))]

Category : Physics > Physics
Formula  : f = f₀ √( (1 − β)/(1 + β) )   (β is the answer of the row above)

Status   : ready to use - call compute(f0, beta)
"""
import math

NAME = 'Relativistic Doppler: frequency'
SYMBOL = 'f = f₀√((1−β)/(1+β))'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'f = f₀ √( (1 − β)/(1 + β) )   (β is the answer of the row above)'


def compute(f0, beta):
    """f = f₀ √( (1 − β)/(1 + β) )"""
    return f0 * math.sqrt((1 - beta) / (1 + beta))
