"""Jacobi iteration   [x⁽ᵏ⁺¹⁾]

Category : Math > Optimization and numerical methods
Formula  : xᵢ⁽ᵏ⁺¹⁾ = (bᵢ − Σ_{j≠i} Aᵢⱼ xⱼ⁽ᵏ⁾) / Aᵢᵢ

Status   : ready to use - call compute(A, b, iterations=100)
"""

NAME = 'Jacobi iteration'
SYMBOL = 'x⁽ᵏ⁺¹⁾'
CATEGORY = 'Math'
SUBCATEGORY = 'Optimization and numerical methods'
FORMULA = 'xᵢ⁽ᵏ⁺¹⁾ = (bᵢ − Σ_{j≠i} Aᵢⱼ xⱼ⁽ᵏ⁾) / Aᵢᵢ'


def compute(A, b, iterations=100):
    """xᵢ⁽ᵏ⁺¹⁾ = (bᵢ − Σ_{j≠i} Aᵢⱼ xⱼ⁽ᵏ⁾) / Aᵢᵢ"""
    n = len(b)
    x = [0.0] * n
    for _ in range(iterations):
        x = [(b[i] - sum(A[i][j] * x[j] for j in range(n) if j != i)) / A[i][i] for i in range(n)]
    return x
