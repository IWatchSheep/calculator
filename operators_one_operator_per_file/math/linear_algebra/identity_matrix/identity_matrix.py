"""Identity matrix   [I]

Category : Math > Linear algebra
Formula  : Iᵢⱼ = 1 if i = j else 0

Status   : ready to use - call compute(n)
"""

NAME = 'Identity matrix'
SYMBOL = 'I'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'Iᵢⱼ = 1 if i = j else 0'


def compute(n):
    """Iᵢⱼ = 1 if i = j else 0"""
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
