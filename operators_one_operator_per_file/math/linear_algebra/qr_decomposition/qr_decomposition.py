"""QR decomposition   [A = QR]

Category : Math > Linear algebra
Formula  : A = Q·R with Q orthogonal (QᵀQ = I) and R upper-triangular

Status   : ready to use - call compute(A)
"""

NAME = 'QR decomposition'
SYMBOL = 'A = QR'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'A = Q·R with Q orthogonal (QᵀQ = I) and R upper-triangular'
import math
from operators_one_operator_per_file import _helpers as H


def compute(A):
    """A = Q·R  (Gram–Schmidt on the columns) → (Q, R)"""
    cols = H.transpose(H.fmat(A))
    n = len(cols)
    q, R = [], [[0.0] * n for _ in range(n)]
    for j, v in enumerate(cols):
        w = list(v)
        for i, qi in enumerate(q):
            R[i][j] = sum(a * b for a, b in zip(qi, v))
            w = [x - R[i][j] * y for x, y in zip(w, qi)]
        R[j][j] = math.sqrt(sum(x * x for x in w))
        if R[j][j] < 1e-12:
            raise ValueError("the columns are not independent")
        q.append([x / R[j][j] for x in w])
    return H.transpose(q), R
