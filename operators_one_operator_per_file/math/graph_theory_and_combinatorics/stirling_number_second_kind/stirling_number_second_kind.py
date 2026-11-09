"""Stirling number (second kind)   [S(n, k)]

Category : Math > Graph theory and combinatorics
Formula  : S(n, k) = (1/k!) Σⱼ (−1)ʲ C(k, j) (k − j)ⁿ

Status   : ready to use - call compute(n, k)
"""
import math

NAME = 'Stirling number (second kind)'
SYMBOL = 'S(n, k)'
CATEGORY = 'Math'
SUBCATEGORY = 'Graph theory and combinatorics'
FORMULA = 'S(n, k) = (1/k!) Σⱼ (−1)ʲ C(k, j) (k − j)ⁿ'


def compute(n, k):
    """S(n, k) = (1/k!) Σⱼ (−1)ʲ C(k, j) (k − j)ⁿ"""
    return sum((-1) ** j * math.comb(k, j) * (k - j) ** n for j in range(k + 1)) // math.factorial(k)
