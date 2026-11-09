"""Golden ratio   [φ]

Category : Math > Constants and relations
Formula  : φ = (1 + √5) / 2 ≈ 1.6180339887…

Status   : ready to use - call compute()
"""
import math

NAME = 'Golden ratio'
SYMBOL = 'φ'
CATEGORY = 'Math'
SUBCATEGORY = 'Constants and relations'
FORMULA = 'φ = (1 + √5) / 2 ≈ 1.6180339887…'


def compute():
    """φ = (1 + √5) / 2 ≈ 1.6180339887…"""
    return (1 + math.sqrt(5)) / 2
