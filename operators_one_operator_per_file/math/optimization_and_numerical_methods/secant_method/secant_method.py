"""Secant method   [secant]

Category : Math > Optimization and numerical methods
Formula  : xₙ₊₁ = xₙ − f(xₙ)(xₙ − xₙ₋₁) / (f(xₙ) − f(xₙ₋₁))

Status   : ready to use - call compute(f, x0, x1, tol=1e-12, max_iter=100)
"""

NAME = 'Secant method'
SYMBOL = 'secant'
CATEGORY = 'Math'
SUBCATEGORY = 'Optimization and numerical methods'
FORMULA = 'xₙ₊₁ = xₙ − f(xₙ)(xₙ − xₙ₋₁) / (f(xₙ) − f(xₙ₋₁))'


def compute(f, x0, x1, tol=1e-12, max_iter=100):
    """xₙ₊₁ = xₙ − f(xₙ)(xₙ − xₙ₋₁) / (f(xₙ) − f(xₙ₋₁))"""
    for _ in range(max_iter):
        f0, f1 = f(x0), f(x1)
        if f1 == f0:
            break
        x0, x1 = x1, x1 - f1 * (x1 - x0) / (f1 - f0)
        if abs(x1 - x0) < tol:
            return x1
    return x1
