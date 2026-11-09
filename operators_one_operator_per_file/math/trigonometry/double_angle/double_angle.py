"""Double angle   [sin 2θ]

Category : Math > Trigonometry
Formula  : sin 2θ = 2 sin θ cos θ

Status   : ready to use - call compute(theta)
"""
import math

NAME = 'Double angle'
SYMBOL = 'sin 2θ'
CATEGORY = 'Math'
SUBCATEGORY = 'Trigonometry'
FORMULA = 'sin 2θ = 2 sin θ cos θ'


def compute(theta):
    """sin 2θ = 2 sin θ cos θ"""
    return 2 * math.sin(theta) * math.cos(theta)
