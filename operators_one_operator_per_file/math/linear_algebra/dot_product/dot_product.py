"""Dot product   [a·b]

Category : Math > Linear algebra
Formula  : a·b = Σ aᵢbᵢ = |a||b|cos θ

Status   : ready to use - call compute(a, b)
"""

NAME = 'Dot product'
SYMBOL = 'a·b'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'a·b = Σ aᵢbᵢ = |a||b|cos θ'


def compute(a, b):
    """a·b = Σ aᵢbᵢ = |a||b|cos θ"""
    return sum(x * y for x, y in zip(a, b))
