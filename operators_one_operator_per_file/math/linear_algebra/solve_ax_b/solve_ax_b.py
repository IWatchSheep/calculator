"""Solve Ax = b   [Ax = b]

Category : Math > Linear algebra
Formula  : Solve the linear system A·x = b  (Gaussian elimination with partial pivoting)

Status   : ready to use - call compute(A, b)
"""

NAME = 'Solve Ax = b'
SYMBOL = 'Ax = b'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'Solve the linear system A·x = b  (Gaussian elimination with partial pivoting)'


def compute(A, b):
    """Solve the linear system A·x = b  (Gaussian elimination with partial pivoting)"""
    n = len(A)
    M = [list(map(float, row)) + [float(b[i])] for i, row in enumerate(A)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c]))
        if abs(M[p][c]) < 1e-12:
            raise ValueError("matrix is singular")
        M[c], M[p] = M[p], M[c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]
    return x
