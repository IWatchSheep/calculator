"""Generating function   [G(x)]

Category : Math > Graph theory and combinatorics
Formula  : G(x) = Σ aₙ xⁿ  encodes the sequence a₀, a₁, a₂, …

Status   : ready to use - call compute(terms, x)
"""

NAME = 'Generating function'
SYMBOL = 'G(x)'
CATEGORY = 'Math'
SUBCATEGORY = 'Graph theory and combinatorics'
FORMULA = 'G(x) = Σ aₙ xⁿ  encodes the sequence a₀, a₁, a₂, …'
import math
from operators_one_operator_per_file import _helpers as H


def compute(terms, x):
    """G(x) = Σ aₙxⁿ for the terms a₀, a₁, a₂, …"""
    return sum(a * x ** n for n, a in enumerate(terms))
