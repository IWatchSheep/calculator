"""Lensmaker's equation   [1/f = (n−1)(1/R₁ − 1/R₂)]

Category : Physics > Physics
Formula  : f = 1 / ( (n − 1)(1/R₁ − 1/R₂) )   (thin lens in air)

Status   : ready to use - call compute(n, R1, R2)
"""
import math

NAME = "Lensmaker's equation"
SYMBOL = '1/f = (n−1)(1/R₁ − 1/R₂)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'f = 1 / ( (n − 1)(1/R₁ − 1/R₂) )   (thin lens in air)'


def compute(n, R1, R2):
    """f = 1 / ( (n − 1)(1/R₁ − 1/R₂) )   (thin lens in air)"""
    return 1 / ((n - 1) * (1 / R1 - 1 / R2))
