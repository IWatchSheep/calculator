"""Newton interpolation   [N(x)]

Category : Math > Optimization and numerical methods
Formula  : N(x) = c₀ + c₁(x − x₀) + c₂(x − x₀)(x − x₁) + …  (divided differences)

Status   : ready to use - call compute(xs, ys, x)
"""

NAME = 'Newton interpolation'
SYMBOL = 'N(x)'
CATEGORY = 'Math'
SUBCATEGORY = 'Optimization and numerical methods'
FORMULA = 'N(x) = c₀ + c₁(x − x₀) + c₂(x − x₀)(x − x₁) + …  (divided differences)'


def compute(xs, ys, x):
    """N(x) = c₀ + c₁(x − x₀) + c₂(x − x₀)(x − x₁) + …  (divided differences)"""
    n = len(xs)
    coef = list(ys)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (xs[i] - xs[i - j])
    result = coef[-1]
    for i in range(n - 2, -1, -1):
        result = result * (x - xs[i]) + coef[i]
    return result
