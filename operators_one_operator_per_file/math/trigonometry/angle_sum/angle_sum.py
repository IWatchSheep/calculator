"""Angle sum   [sin(a+b)]

Category : Math > Trigonometry
Formula  : sin(a + b) = sin a cos b + cos a sin b

Status   : ready to use - call compute(a, b)
"""
import math

NAME = 'Angle sum'
SYMBOL = 'sin(a+b)'
CATEGORY = 'Math'
SUBCATEGORY = 'Trigonometry'
FORMULA = 'sin(a + b) = sin a cos b + cos a sin b'


def compute(a, b):
    """sin(a + b) = sin a cos b + cos a sin b"""
    return math.sin(a) * math.cos(b) + math.cos(a) * math.sin(b)
