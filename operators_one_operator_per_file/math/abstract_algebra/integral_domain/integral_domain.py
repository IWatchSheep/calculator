"""Integral domain   [ID]

Category : Math > Abstract algebra
Formula  : A commutative ring with 1 ≠ 0 and no zero divisors

Status   : ready to use - call compute(n)
"""

NAME = 'Integral domain'
SYMBOL = 'ID'
CATEGORY = 'Math'
SUBCATEGORY = 'Abstract algebra'
FORMULA = 'A commutative ring with 1 ≠ 0 and no zero divisors'
import math
from operators_one_operator_per_file import _helpers as H


def compute(n):
    """True if the integers mod n form an integral domain (that happens exactly when n is prime)"""
    n = int(n)
    return n >= 2 and all(n % k for k in range(2, int(math.isqrt(n)) + 1))
