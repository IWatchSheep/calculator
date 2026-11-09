"""Snell's law   [n₁sin θ₁ = n₂sin θ₂]

Category : Physics > Physics
Formula  : θ₂ = arcsin(n₁ sin θ₁ / n₂)   (angles in radians)

Status   : ready to use - call compute(n1, theta1, n2)
"""
import math

NAME = "Snell's law"
SYMBOL = 'n₁sin θ₁ = n₂sin θ₂'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'θ₂ = arcsin(n₁ sin θ₁ / n₂)   (angles in radians)'


def compute(n1, theta1, n2):
    """θ₂ = arcsin(n₁ sin θ₁ / n₂)   (angles in radians)"""
    return math.asin(n1 * math.sin(theta1) / n2)
