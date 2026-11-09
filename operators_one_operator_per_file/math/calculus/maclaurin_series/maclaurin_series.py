"""Maclaurin series   [Σ f⁽ⁿ⁾(0)/n!]

Category : Math > Calculus
Formula  : f(x) ≈ Σₙ f⁽ⁿ⁾(0)/n! · xⁿ   (Taylor series about 0)

Status   : ready to use - call compute(derivs, x)
"""
import math

NAME = 'Maclaurin series'
SYMBOL = 'Σ f⁽ⁿ⁾(0)/n!'
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = 'f(x) ≈ Σₙ f⁽ⁿ⁾(0)/n! · xⁿ   (Taylor series about 0)'


def compute(derivs, x):
    """f(x) ≈ Σₙ f⁽ⁿ⁾(0)/n! · xⁿ   (Taylor series about 0)"""
    return sum(d / math.factorial(n) * x ** n for n, d in enumerate(derivs))
