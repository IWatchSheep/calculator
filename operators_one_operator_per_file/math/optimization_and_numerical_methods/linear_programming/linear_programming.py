"""Linear programming   [LP]

Category : Math > Optimization and numerical methods
Formula  : Maximize cᵀx subject to Ax ≤ b, x ≥ 0

Status   : ready to use - call compute(c, A, b)
"""

NAME = 'Linear programming'
SYMBOL = 'LP'
CATEGORY = 'Math'
SUBCATEGORY = 'Optimization and numerical methods'
FORMULA = 'Maximize cᵀx subject to Ax ≤ b, x ≥ 0'
import math
from operators_one_operator_per_file import _helpers as H


def compute(c, A, b):
    """Maximize c·x subject to A·x ≤ b, x ≥ 0 (b ≥ 0)  → (x, best value)"""
    m, n = len(A), len(c)
    if any(v < 0 for v in b):
        raise ValueError("every b must be ≥ 0")
    T = [list(map(float, A[i])) + [1.0 if j == i else 0.0 for j in range(m)] + [float(b[i])] for i in range(m)]
    T.append([-float(v) for v in c] + [0.0] * m + [0.0])
    for _ in range(500):
        col = min(range(n + m), key=lambda j: T[-1][j])
        if T[-1][col] >= -1e-12:
            break
        rows = [(T[i][-1] / T[i][col], i) for i in range(m) if T[i][col] > 1e-12]
        if not rows:
            raise ValueError("the problem is unbounded")
        _ratio, r = min(rows)
        piv = T[r][col]
        T[r] = [v / piv for v in T[r]]
        for i in range(m + 1):
            if i != r:
                f = T[i][col]
                T[i] = [a - f * bb for a, bb in zip(T[i], T[r])]
    x = [0.0] * n
    for j in range(n):
        ones = [i for i in range(m) if abs(T[i][j] - 1) < 1e-9 and all(abs(T[k][j]) < 1e-9 for k in range(m) if k != i)]
        if ones:
            x[j] = T[ones[0]][-1]
    return x, T[-1][-1]
