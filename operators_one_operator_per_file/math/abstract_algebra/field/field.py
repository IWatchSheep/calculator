"""Field   [F]

Category : Math > Abstract algebra
Formula  : A commutative ring where every non-zero element has a multiplicative inverse

Status   : ready to use - call compute(n)
"""

NAME = 'Field'
SYMBOL = 'F'
CATEGORY = 'Math'
SUBCATEGORY = 'Abstract algebra'
FORMULA = 'A commutative ring where every non-zero element has a multiplicative inverse'
import math
from operators_one_operator_per_file import _helpers as H


def compute(n):
    """True if the integers mod n form a field (that happens exactly when n is prime)"""
    n = int(n)
    return n >= 2 and all(n % k for k in range(2, int(math.isqrt(n)) + 1))
