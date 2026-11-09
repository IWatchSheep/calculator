"""t-test statistic   [t]

Category : Math > Statistics and probability
Formula  : t = (x̄ − μ₀) / (s / √n)   (one-sample)

Status   : ready to use - call compute(mean, mu0, s, n)
"""
import math

NAME = 't-test statistic'
SYMBOL = 't'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 't = (x̄ − μ₀) / (s / √n)   (one-sample)'


def compute(mean, mu0, s, n):
    """t = (x̄ − μ₀) / (s / √n)   (one-sample)"""
    return (mean - mu0) / (s / math.sqrt(n))
