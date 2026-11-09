"""Fixed-point iteration   [x = g(x)]

Category : Math > Optimization and numerical methods
Formula  : xₙ₊₁ = g(xₙ)

Status   : ready to use - call compute(g, x0, tol=1e-12, max_iter=1000)
"""

NAME = 'Fixed-point iteration'
SYMBOL = 'x = g(x)'
CATEGORY = 'Math'
SUBCATEGORY = 'Optimization and numerical methods'
FORMULA = 'xₙ₊₁ = g(xₙ)'


def compute(g, x0, tol=1e-12, max_iter=1000):
    """xₙ₊₁ = g(xₙ)"""
    x = x0
    for _ in range(max_iter):
        nx = g(x)
        if abs(nx - x) < tol:
            return nx
        x = nx
    raise RuntimeError("fixed-point iteration did not converge")
