"""Order of element   [ord(g)]

Category : Math > Abstract algebra
Formula  : smallest k > 0 with gᵏ = e   (op = the group operation)

Status   : ready to use - call compute(g, op, identity)
"""

NAME = 'Order of element'
SYMBOL = 'ord(g)'
CATEGORY = 'Math'
SUBCATEGORY = 'Abstract algebra'
FORMULA = 'smallest k > 0 with gᵏ = e   (op = the group operation)'


def compute(g, op, identity):
    """smallest k > 0 with gᵏ = e   (op = the group operation)"""
    x, k = g, 1
    while x != identity:
        x = op(x, g)
        k += 1
    return k
