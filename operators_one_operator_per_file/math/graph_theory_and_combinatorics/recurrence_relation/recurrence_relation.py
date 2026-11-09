"""Recurrence relation   [aₙ = f(aₙ₋₁, …)]

Category : Math > Graph theory and combinatorics
Formula  : Defines each term from earlier terms, e.g. Fibonacci Fₙ = Fₙ₋₁ + Fₙ₋₂

Status   : ready to use - call compute(coeffs, start, n)
"""

NAME = 'Recurrence relation'
SYMBOL = 'aₙ = f(aₙ₋₁, …)'
CATEGORY = 'Math'
SUBCATEGORY = 'Graph theory and combinatorics'
FORMULA = 'Defines each term from earlier terms, e.g. Fibonacci Fₙ = Fₙ₋₁ + Fₙ₋₂'
import math
from operators_one_operator_per_file import _helpers as H


def compute(coeffs, start, n):
    """The n-th term (counting from 0) of aₖ = c₁aₖ₋₁ + c₂aₖ₋₂ + …  given the first terms.  Fibonacci: coeffs 1, 1  start 0, 1"""
    n = int(n)
    a = list(start)
    if len(a) < len(coeffs):
        raise ValueError("give at least as many starting terms as coefficients")
    while len(a) <= n:
        a.append(sum(c * a[-1 - i] for i, c in enumerate(coeffs)))
    return a[n]
