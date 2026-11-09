"""Modular arithmetic   [a mod m]

Category : Math > Discrete and number theory
Formula  : a ≡ r (mod m) where r = a − m·⌊a/m⌋

Status   : ready to use - call compute(a, m)
"""

NAME = 'Modular arithmetic'
SYMBOL = 'a mod m'
CATEGORY = 'Math'
SUBCATEGORY = 'Discrete and number theory'
FORMULA = 'a ≡ r (mod m) where r = a − m·⌊a/m⌋'


def compute(a, m):
    """a ≡ r (mod m) where r = a − m·⌊a/m⌋"""
    return a % m
