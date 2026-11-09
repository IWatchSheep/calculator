"""Vector magnitude   [‖v‖]

Category : Math > Linear algebra
Formula  : ‖v‖ = √(v₁² + v₂² + …)

Status   : ready to use - call compute(v)
"""
import math

NAME = 'Vector magnitude'
SYMBOL = '‖v‖'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = '‖v‖ = √(v₁² + v₂² + …)'


def compute(v):
    """‖v‖ = √(v₁² + v₂² + …)"""
    return math.hypot(*v)
