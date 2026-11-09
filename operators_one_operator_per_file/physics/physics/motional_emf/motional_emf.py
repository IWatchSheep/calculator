"""Motional emf   [ε = BLv]

Category : Physics > Physics
Formula  : ε = B L v   (rod of length L moving at speed v across B)

Status   : ready to use - call compute(B, L, v)
"""
import math

NAME = 'Motional emf'
SYMBOL = 'ε = BLv'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'ε = B L v   (rod of length L moving at speed v across B)'


def compute(B, L, v):
    """ε = B L v   (rod of length L moving at speed v across B)"""
    return B * L * v
