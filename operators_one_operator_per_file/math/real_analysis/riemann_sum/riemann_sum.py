"""Riemann sum   [Σ f(xᵢ)Δx]

Category : Math > Real analysis
Formula  : Σ f(xᵢ) · Δx   (left endpoints, n subintervals)

Status   : ready to use - call compute(f, a, b, n)
"""

NAME = 'Riemann sum'
SYMBOL = 'Σ f(xᵢ)Δx'
CATEGORY = 'Math'
SUBCATEGORY = 'Real analysis'
FORMULA = 'Σ f(xᵢ) · Δx   (left endpoints, n subintervals)'


def compute(f, a, b, n):
    """Σ f(xᵢ) · Δx   (left endpoints, n subintervals)"""
    return sum(f(a + i * (b - a) / n) for i in range(n)) * (b - a) / n
