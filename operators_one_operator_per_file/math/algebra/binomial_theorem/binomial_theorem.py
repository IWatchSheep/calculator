"""Binomial theorem   [(a+b)ⁿ]

Category : Math > Algebra
Formula  : (a + b)ⁿ = Σₖ C(n,k) · aⁿ⁻ᵏ · bᵏ

Status   : ready to use - call compute(a, b, n)
"""
import math

NAME = 'Binomial theorem'
SYMBOL = '(a+b)ⁿ'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = '(a + b)ⁿ = Σₖ C(n,k) · aⁿ⁻ᵏ · bᵏ'


def compute(a, b, n):
    """(a + b)ⁿ = Σₖ C(n,k) · aⁿ⁻ᵏ · bᵏ"""
    return sum(math.comb(n, k) * a ** (n - k) * b ** k for k in range(n + 1))
