"""Quotient group order   [G/N]

Category : Math > Abstract algebra
Formula  : |G/N| = |G| / |N|

Status   : ready to use - call compute(order_g, order_n)
"""

NAME = 'Quotient group order'
SYMBOL = 'G/N'
CATEGORY = 'Math'
SUBCATEGORY = 'Abstract algebra'
FORMULA = '|G/N| = |G| / |N|'


def compute(order_g, order_n):
    """|G/N| = |G| / |N|"""
    return order_g // order_n
