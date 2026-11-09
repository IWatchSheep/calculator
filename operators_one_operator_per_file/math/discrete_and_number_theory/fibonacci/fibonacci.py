"""Fibonacci   [Fₙ]

Category : Math > Discrete and number theory
Formula  : F₀ = 0, F₁ = 1, Fₙ = Fₙ₋₁ + Fₙ₋₂

Status   : ready to use - call compute(n)
"""

NAME = 'Fibonacci'
SYMBOL = 'Fₙ'
CATEGORY = 'Math'
SUBCATEGORY = 'Discrete and number theory'
FORMULA = 'F₀ = 0, F₁ = 1, Fₙ = Fₙ₋₁ + Fₙ₋₂'


def compute(n):
    """F₀ = 0, F₁ = 1, Fₙ = Fₙ₋₁ + Fₙ₋₂"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
