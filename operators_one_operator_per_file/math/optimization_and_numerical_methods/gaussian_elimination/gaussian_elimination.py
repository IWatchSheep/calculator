"""Gaussian elimination   [A|b → U]

Category : Math > Optimization and numerical methods
Formula  : Reduce [A | b] to upper-triangular form, then back-substitute

Status   : ready to use - call compute(A, b)
"""

NAME = 'Gaussian elimination'
SYMBOL = 'A|b → U'
CATEGORY = 'Math'
SUBCATEGORY = 'Optimization and numerical methods'
FORMULA = 'Reduce [A | b] to upper-triangular form, then back-substitute'


def compute(A, b):
    """Reduce [A | b] to upper-triangular form, then back-substitute"""
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
