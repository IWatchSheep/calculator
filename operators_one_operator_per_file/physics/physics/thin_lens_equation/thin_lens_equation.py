"""Thin lens equation   [1/f = 1/dₒ + 1/dᵢ]

Category : Physics > Physics
Formula  : dᵢ = 1 / (1/f − 1/dₒ)   (returns the image distance, real-is-positive)

Status   : ready to use - call compute(f, d_o)
"""
import math

NAME = 'Thin lens equation'
SYMBOL = '1/f = 1/dₒ + 1/dᵢ'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'dᵢ = 1 / (1/f − 1/dₒ)   (returns the image distance, real-is-positive)'


def compute(f, d_o):
    """dᵢ = 1 / (1/f − 1/dₒ)   (returns the image distance, real-is-positive)"""
    return 1 / (1 / f - 1 / d_o)
