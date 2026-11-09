"""Tensor product   [⊗]

Category : Math > Abstract algebra
Formula  : (a ⊗ b) = (a₁b₁, a₁b₂, …, aₘbₙ)   (Kronecker product of two vectors)

Status   : ready to use - call compute(a, b)
"""

NAME = 'Tensor product'
SYMBOL = '⊗'
CATEGORY = 'Math'
SUBCATEGORY = 'Abstract algebra'
FORMULA = '(a ⊗ b) = (a₁b₁, a₁b₂, …, aₘbₙ)   (Kronecker product of two vectors)'


def compute(a, b):
    """(a ⊗ b) = (a₁b₁, a₁b₂, …, aₘbₙ)   (Kronecker product of two vectors)"""
    return [x * y for x in a for y in b]
