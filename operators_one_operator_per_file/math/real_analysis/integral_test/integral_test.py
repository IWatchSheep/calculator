"""Integral test   [∫ vs Σ]

Category : Math > Real analysis
Formula  : For positive decreasing f, Σ f(n) and ∫ f(x) dx converge or diverge together

Status   : ready to use - call compute(f, N)
"""

NAME = 'Integral test'
SYMBOL = '∫ vs Σ'
CATEGORY = 'Math'
SUBCATEGORY = 'Real analysis'
FORMULA = 'For positive decreasing f, Σ f(n) and ∫ f(x) dx converge or diverge together'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, N):
    """For positive decreasing f: (Σ f(n) for n = 1…N, ∫ of f from 1 to N) — they grow together or stay bounded together"""
    N = int(N)
    return sum(f(n) for n in range(1, N + 1)), H.simpson(f, 1, N, 2000)
