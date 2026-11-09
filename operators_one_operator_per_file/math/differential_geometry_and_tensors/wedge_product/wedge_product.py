"""Wedge product   [∧]

Category : Math > Differential geometry and tensors
Formula  : α ∧ β = −β ∧ α  (antisymmetric product of differential forms)

Status   : ready to use - call compute(a, b)
"""

NAME = 'Wedge product'
SYMBOL = '∧'
CATEGORY = 'Math'
SUBCATEGORY = 'Differential geometry and tensors'
FORMULA = 'α ∧ β = −β ∧ α  (antisymmetric product of differential forms)'
import math
from operators_one_operator_per_file import _helpers as H


def compute(a, b):
    """α ∧ β for two 1-forms (vectors): the components aᵢbⱼ − aⱼbᵢ for i < j"""
    n = len(a)
    return [a[i] * b[j] - a[j] * b[i] for i in range(n) for j in range(i + 1, n)]
