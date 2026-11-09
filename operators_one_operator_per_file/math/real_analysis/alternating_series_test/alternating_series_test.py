"""Alternating series test   [Σ (−1)ⁿ aₙ]

Category : Math > Real analysis
Formula  : Converges if aₙ decreases to 0

Status   : ready to use - call compute(terms)
"""

NAME = 'Alternating series test'
SYMBOL = 'Σ (−1)ⁿ aₙ'
CATEGORY = 'Math'
SUBCATEGORY = 'Real analysis'
FORMULA = 'Converges if aₙ decreases to 0'
import math
from operators_one_operator_per_file import _helpers as H


def compute(terms):
    """Terms bₙ = |aₙ| of an alternating series Σ(−1)ⁿbₙ → (are they decreasing?, the last term)  — decreasing to 0 means it converges"""
    b = [abs(t) for t in terms]
    return all(b[i + 1] <= b[i] for i in range(len(b) - 1)), b[-1]
