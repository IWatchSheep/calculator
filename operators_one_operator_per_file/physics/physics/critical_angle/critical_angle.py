"""Critical angle (total internal reflection)   [θc = arcsin(n₂/n₁)]

Category : Physics > Physics
Formula  : θc = arcsin(n₂ / n₁)   (n₁ > n₂, angle in radians)

Status   : ready to use - call compute(n1, n2)
"""
import math

NAME = 'Critical angle (total internal reflection)'
SYMBOL = 'θc = arcsin(n₂/n₁)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'θc = arcsin(n₂ / n₁)   (n₁ > n₂, angle in radians)'


def compute(n1, n2):
    """θc = arcsin(n₂ / n₁)   (n₁ > n₂, angle in radians)"""
    if n1 <= n2:
        raise ValueError('total internal reflection needs n1 > n2')
    return math.asin(n2 / n1)
