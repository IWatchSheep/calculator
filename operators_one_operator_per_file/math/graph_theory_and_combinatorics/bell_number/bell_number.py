"""Bell number   [Bₙ]

Category : Math > Graph theory and combinatorics
Formula  : Bₙ = Σₖ S(n, k)   (number of partitions of an n-element set)

Status   : ready to use - call compute(n)
"""
import math

NAME = 'Bell number'
SYMBOL = 'Bₙ'
CATEGORY = 'Math'
SUBCATEGORY = 'Graph theory and combinatorics'
FORMULA = 'Bₙ = Σₖ S(n, k)   (number of partitions of an n-element set)'


def compute(n):
    """Bₙ = Σₖ S(n, k)   (number of partitions of an n-element set)"""
    return sum(sum((-1) ** j * math.comb(k, j) * (k - j) ** n for j in range(k + 1)) // math.factorial(k) for k in range(n + 1))
