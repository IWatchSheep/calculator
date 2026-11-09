"""Newton's method   [xₙ₊₁ = xₙ − f/f′]

Category : Math > Optimization and numerical methods
Formula  : xₙ₊₁ = xₙ − f(xₙ) / f′(xₙ)

Status   : ready to use - call compute(f, fprime, x0, tol=1e-12, max_iter=100)
"""

NAME = "Newton's method"
SYMBOL = 'xₙ₊₁ = xₙ − f/f′'
CATEGORY = 'Math'
SUBCATEGORY = 'Optimization and numerical methods'
FORMULA = 'xₙ₊₁ = xₙ − f(xₙ) / f′(xₙ)'


def compute(f, fprime, x0, tol=1e-12, max_iter=100):
    """xₙ₊₁ = xₙ − f(xₙ) / f′(xₙ)"""
    x = x0
    for _ in range(max_iter):
        step = f(x) / fprime(x)
        x -= step
        if abs(step) < tol:
            return x
    raise RuntimeError("Newton's method did not converge")
