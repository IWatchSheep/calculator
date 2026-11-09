"""Hooke's law   [F = −kx]

Category : Physics > Physics
Formula  : F = −k x

Status   : ready to use - call compute(k, x)
"""

NAME = "Hooke's law"
SYMBOL = 'F = −kx'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'F = −k x'


def compute(k, x):
    """F = −k x"""
    return -k * x
