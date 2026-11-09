"""Matrix subtract   [A − B]

Category : Math > Linear algebra
Formula  : (A − B)ᵢⱼ = Aᵢⱼ − Bᵢⱼ

Status   : ready to use - call compute(A, B)
"""

NAME = 'Matrix subtract'
SYMBOL = 'A − B'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = '(A − B)ᵢⱼ = Aᵢⱼ − Bᵢⱼ'


def compute(A, B):
    """(A − B)ᵢⱼ = Aᵢⱼ − Bᵢⱼ"""
    return [[x - y for x, y in zip(r1, r2)] for r1, r2 in zip(A, B)]
