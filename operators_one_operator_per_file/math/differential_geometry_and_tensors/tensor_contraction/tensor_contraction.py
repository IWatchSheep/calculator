"""Tensor contraction   [Tⁱᵢ]

Category : Math > Differential geometry and tensors
Formula  : Sum over a paired upper and lower index, lowering the tensor's rank by 2

Status   : ready to use - call compute(T)
"""

NAME = 'Tensor contraction'
SYMBOL = 'Tⁱᵢ'
CATEGORY = 'Math'
SUBCATEGORY = 'Differential geometry and tensors'
FORMULA = "Sum over a paired upper and lower index, lowering the tensor's rank by 2"
import math
from operators_one_operator_per_file import _helpers as H


def compute(T):
    """Contract the two indices of a rank-2 tensor (a matrix): the trace Σ Tⁱᵢ"""
    return sum(T[i][i] for i in range(len(T)))
