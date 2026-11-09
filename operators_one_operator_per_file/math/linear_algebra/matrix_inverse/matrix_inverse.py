"""Matrix inverse   [A⁻¹]

Category : Math > Linear algebra
Formula  : A·A⁻¹ = I   (Gauss–Jordan elimination)

Status   : ready to use - call compute(A)
"""

NAME = 'Matrix inverse'
SYMBOL = 'A⁻¹'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'A·A⁻¹ = I   (Gauss–Jordan elimination)'


def compute(A):
    """A·A⁻¹ = I   (Gauss–Jordan elimination)"""
    n = len(A)
    M = [list(map(float, row)) + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(A)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c]))
        if abs(M[p][c]) < 1e-12:
            raise ValueError("matrix is singular")
        M[c], M[p] = M[p], M[c]
        pivot = M[c][c]
        M[c] = [x / pivot for x in M[c]]
        for r in range(n):
            if r != c:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [row[n:] for row in M]
