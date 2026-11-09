"""Vector projection   [proj_b a]

Category : Math > Linear algebra
Formula  : proj_b(a) = (a·b / b·b) · b

Status   : ready to use - call compute(a, b)
"""

NAME = 'Vector projection'
SYMBOL = 'proj_b a'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'proj_b(a) = (a·b / b·b) · b'


def compute(a, b):
    """proj_b(a) = (a·b / b·b) · b"""
    return [sum(x * y for x, y in zip(a, b)) / sum(y * y for y in b) * y for y in b]
