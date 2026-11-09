"""Row reduce (RREF)   [RREF]

Category : Math > Linear algebra
Formula  : Reduced row echelon form via Gauss–Jordan elimination

Status   : ready to use - call compute(A)
"""

NAME = 'Row reduce (RREF)'
SYMBOL = 'RREF'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'Reduced row echelon form via Gauss–Jordan elimination'


def compute(A):
    """Reduced row echelon form via Gauss–Jordan elimination"""
    M = [list(map(float, r)) for r in A]
    rows, cols = len(M), len(M[0])
    r = 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if abs(M[i][c]) > 1e-12), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pivot = M[r][c]
        M[r] = [x / pivot for x in M[r]]
        for i in range(rows):
            if i != r:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        r += 1
        if r == rows:
            break
    return M
