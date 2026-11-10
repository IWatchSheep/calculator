"""Spin up along z   [P(↑_z)]

Category : Physics > Physics
Formula  : P(↑_z) = 1 if the spin-1/2 particle was prepared spin up along z, 0 if it was prepared spin down (the prepared value is 1 or −1)

Status   : ready to use - call compute(prepared)
"""
NAME = 'Spin up along z'
SYMBOL = 'P(↑_z)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'P(↑_z) = 1 if the spin-1/2 particle was prepared spin up along z, 0 if it was prepared spin down (the prepared value is 1 or −1)'


def compute(prepared):
    """1 or 0"""
    if prepared not in (1, -1):
        raise ValueError("the prepared spin must be 1 or -1")
    return 1.0 if prepared == 1 else 0.0
