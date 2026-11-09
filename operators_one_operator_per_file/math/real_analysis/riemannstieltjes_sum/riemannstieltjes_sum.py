"""Riemann–Stieltjes sum   [∫ f dg]

Category : Math > Real analysis
Formula  : Σ f(xᵢ) · (g(xᵢ₊₁) − g(xᵢ))

Status   : ready to use - call compute(f, g, xs)
"""

NAME = 'Riemann–Stieltjes sum'
SYMBOL = '∫ f dg'
CATEGORY = 'Math'
SUBCATEGORY = 'Real analysis'
FORMULA = 'Σ f(xᵢ) · (g(xᵢ₊₁) − g(xᵢ))'


def compute(f, g, xs):
    """Σ f(xᵢ) · (g(xᵢ₊₁) − g(xᵢ))"""
    return sum(f(xs[i]) * (g(xs[i + 1]) - g(xs[i])) for i in range(len(xs) - 1))
