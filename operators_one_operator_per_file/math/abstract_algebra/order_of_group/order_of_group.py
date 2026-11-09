"""Order of group   [|G|]

Category : Math > Abstract algebra
Formula  : |G| = number of elements of G

Status   : ready to use - call compute(elements)
"""

NAME = 'Order of group'
SYMBOL = '|G|'
CATEGORY = 'Math'
SUBCATEGORY = 'Abstract algebra'
FORMULA = '|G| = number of elements of G'


def compute(elements):
    """|G| = number of elements of G"""
    return len(set(elements))
