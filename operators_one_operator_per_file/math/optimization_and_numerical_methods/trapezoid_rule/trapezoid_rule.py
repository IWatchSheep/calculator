"""Trapezoid rule   [T]

Category : Math > Optimization and numerical methods
Formula  : ∫ₐᵇ f ≈ h · (f(a)/2 + Σ f(xᵢ) + f(b)/2),  h = (b − a)/n

Status   : ready to use - call compute(f, a, b, n=1000)
"""

NAME = 'Trapezoid rule'
SYMBOL = 'T'
CATEGORY = 'Math'
SUBCATEGORY = 'Optimization and numerical methods'
FORMULA = '∫ₐᵇ f ≈ h · (f(a)/2 + Σ f(xᵢ) + f(b)/2),  h = (b − a)/n'


def compute(f, a, b, n=1000):
    """∫ₐᵇ f ≈ h · (f(a)/2 + Σ f(xᵢ) + f(b)/2),  h = (b − a)/n"""
    return (b - a) / n * ((f(a) + f(b)) / 2 + sum(f(a + i * (b - a) / n) for i in range(1, n)))
