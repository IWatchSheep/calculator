"""Cross product   [a×b]

Category : Math > Linear algebra
Formula  : a × b = (a₂b₃ − a₃b₂, a₃b₁ − a₁b₃, a₁b₂ − a₂b₁)   (3D vectors)

Status   : ready to use - call compute(a, b)
"""

NAME = 'Cross product'
SYMBOL = 'a×b'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'a × b = (a₂b₃ − a₃b₂, a₃b₁ − a₁b₃, a₁b₂ − a₂b₁)   (3D vectors)'


def compute(a, b):
    """a × b = (a₂b₃ − a₃b₂, a₃b₁ − a₁b₃, a₁b₂ − a₂b₁)   (3D vectors)"""
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
