"""Half angle   [sin θ/2]

Category : Math > Trigonometry
Formula  : sin(θ/2) = √((1 − cos θ) / 2)   (for θ/2 in the first two quadrants)

Status   : ready to use - call compute(theta)
"""
import math

NAME = 'Half angle'
SYMBOL = 'sin θ/2'
CATEGORY = 'Math'
SUBCATEGORY = 'Trigonometry'
FORMULA = 'sin(θ/2) = √((1 − cos θ) / 2)   (for θ/2 in the first two quadrants)'


def compute(theta):
    """sin(θ/2) = √((1 − cos θ) / 2)   (for θ/2 in the first two quadrants)"""
    return math.sqrt((1 - math.cos(theta)) / 2)
