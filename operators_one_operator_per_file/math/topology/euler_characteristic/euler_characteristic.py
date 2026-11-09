"""Euler characteristic   [χ]

Category : Math > Topology
Formula  : χ = V − E + F   (vertices − edges + faces)

Status   : ready to use - call compute(v, e, f)
"""

NAME = 'Euler characteristic'
SYMBOL = 'χ'
CATEGORY = 'Math'
SUBCATEGORY = 'Topology'
FORMULA = 'χ = V − E + F   (vertices − edges + faces)'


def compute(v, e, f):
    """χ = V − E + F   (vertices − edges + faces)"""
    return v - e + f
