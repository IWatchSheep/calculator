"""Taylor series   [Σ f⁽ⁿ⁾(a)/n!]

Category : Math > Calculus
Formula  : f(x) ≈ Σₙ f⁽ⁿ⁾(a)/n! · (x − a)ⁿ   (derivs = [f(a), f′(a), f″(a), …])

Status   : ready to use - call compute(derivs, a, x)
"""
import math

NAME = 'Taylor series'
SYMBOL = 'Σ f⁽ⁿ⁾(a)/n!'
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = 'f(x) ≈ Σₙ f⁽ⁿ⁾(a)/n! · (x − a)ⁿ   (derivs = [f(a), f′(a), f″(a), …])'


def compute(derivs, a, x):
    """f(x) ≈ Σₙ f⁽ⁿ⁾(a)/n! · (x − a)ⁿ   (derivs = [f(a), f′(a), f″(a), …])"""
    return sum(d / math.factorial(n) * (x - a) ** n for n, d in enumerate(derivs))
