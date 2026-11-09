"""Metric tensor   [g]

Category : Math > Differential geometry and tensors
Formula  : gᵢⱼ gives lengths and angles: ds² = gᵢⱼ dxⁱ dxʲ

Status   : ready to use - call compute(g, v, w)
"""

NAME = 'Metric tensor'
SYMBOL = 'g'
CATEGORY = 'Math'
SUBCATEGORY = 'Differential geometry and tensors'
FORMULA = 'gᵢⱼ gives lengths and angles: ds² = gᵢⱼ dxⁱ dxʲ'
import math
from operators_one_operator_per_file import _helpers as H


def compute(g, v, w):
    """gᵢⱼ vⁱ wʲ: the inner product of two vectors with the metric g (a matrix)"""
    return sum(v[i] * g[i][j] * w[j] for i in range(len(v)) for j in range(len(w)))
