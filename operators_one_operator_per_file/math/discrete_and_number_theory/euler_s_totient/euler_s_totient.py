"""Euler's totient   [φ(n)]

Category : Math > Discrete and number theory
Formula  : φ(n) = number of integers in 1…n that are coprime to n = n · ∏(1 − 1/p)

Status   : ready to use - call compute(n)
"""

NAME = "Euler's totient"
SYMBOL = 'φ(n)'
CATEGORY = 'Math'
SUBCATEGORY = 'Discrete and number theory'
FORMULA = 'φ(n) = number of integers in 1…n that are coprime to n = n · ∏(1 − 1/p)'


def compute(n):
    """φ(n) = number of integers in 1…n that are coprime to n = n · ∏(1 − 1/p)"""
    result = n
    m = n
    p = 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            result -= result // p
        p += 1
    if m > 1:
        result -= result // m
    return result
