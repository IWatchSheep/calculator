"""Series convergence test   [Σ aₙ]

Category : Math > Real analysis
Formula  : Σ aₙ converges if its partial sums converge; use the ratio/root/comparison/integral tests

Status   : ready to use - call compute(terms)
"""

NAME = 'Series convergence test'
SYMBOL = 'Σ aₙ'
CATEGORY = 'Math'
SUBCATEGORY = 'Real analysis'
FORMULA = 'Σ aₙ converges if its partial sums converge; use the ratio/root/comparison/integral tests'
import math
from operators_one_operator_per_file import _helpers as H


def compute(terms):
    """Ratio test on the last two terms → (|aₙ₊₁/aₙ|, verdict)"""
    r = abs(terms[-1] / terms[-2])
    return r, ("converges (ratio < 1)" if r < 1 else "diverges (ratio > 1)" if r > 1 else "inconclusive (ratio = 1)")
