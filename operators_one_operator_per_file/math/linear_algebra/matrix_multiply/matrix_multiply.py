"""Matrix multiply   [A·B]

Category : Math > Linear algebra
Formula  : (AB)ᵢⱼ = Σₖ Aᵢₖ · Bₖⱼ

Status   : ready to use - call compute(A, B)
"""

NAME = 'Matrix multiply'
SYMBOL = 'A·B'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = '(AB)ᵢⱼ = Σₖ Aᵢₖ · Bₖⱼ'


def compute(A, B):
    """(AB)ᵢⱼ = Σₖ Aᵢₖ · Bₖⱼ"""
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]
