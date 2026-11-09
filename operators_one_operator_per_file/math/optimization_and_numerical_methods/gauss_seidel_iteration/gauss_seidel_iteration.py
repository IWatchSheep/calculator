"""Gauss-Seidel iteration   [x⁽ᵏ⁺¹⁾]

Category : Math > Optimization and numerical methods
Formula  : Like Jacobi but uses the newest values immediately

Status   : ready to use - call compute(A, b, iterations=100)
"""

NAME = 'Gauss-Seidel iteration'
SYMBOL = 'x⁽ᵏ⁺¹⁾'
CATEGORY = 'Math'
SUBCATEGORY = 'Optimization and numerical methods'
FORMULA = 'Like Jacobi but uses the newest values immediately'


def compute(A, b, iterations=100):
    """Like Jacobi but uses the newest values immediately"""
    n = len(b)
    x = [0.0] * n
    for _ in range(iterations):
        for i in range(n):
            x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(n) if j != i)) / A[i][i]
    return x
