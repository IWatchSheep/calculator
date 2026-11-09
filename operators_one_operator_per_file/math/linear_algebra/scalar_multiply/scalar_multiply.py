"""Scalar multiply   [kA]

Category : Math > Linear algebra
Formula  : (kA)ᵢⱼ = k · Aᵢⱼ

Status   : ready to use - call compute(k, A)
"""

NAME = 'Scalar multiply'
SYMBOL = 'kA'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = '(kA)ᵢⱼ = k · Aᵢⱼ'


def compute(k, A):
    """(kA)ᵢⱼ = k · Aᵢⱼ"""
    return [[k * x for x in row] for row in A]
