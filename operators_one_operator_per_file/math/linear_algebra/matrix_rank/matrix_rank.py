"""Matrix rank   [rank(A)]

Category : Math > Linear algebra
Formula  : rank(A) = number of linearly independent rows (pivots after elimination)

Status   : ready to use - call compute(A)
"""

NAME = 'Matrix rank'
SYMBOL = 'rank(A)'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'rank(A) = number of linearly independent rows (pivots after elimination)'


def compute(A):
    """rank(A) = number of linearly independent rows (pivots after elimination)"""
    M = [list(map(float, r)) for r in A]
    rows, cols = len(M), len(M[0])
    rank = 0
    for c in range(cols):
        p = next((r for r in range(rank, rows) if abs(M[r][c]) > 1e-12), None)
        if p is None:
            continue
        M[rank], M[p] = M[p], M[rank]
        for r in range(rank + 1, rows):
            f = M[r][c] / M[rank][c]
            M[r] = [x - f * y for x, y in zip(M[r], M[rank])]
        rank += 1
    return rank
