"""Greatest common divisor   [gcd]

Category : Math > Discrete and number theory
Formula  : largest integer dividing both a and b

Status   : ready to use - call compute(a, b)
"""
import math

NAME = 'Greatest common divisor'
SYMBOL = 'gcd'
CATEGORY = 'Math'
SUBCATEGORY = 'Discrete and number theory'
FORMULA = 'largest integer dividing both a and b'


def compute(a, b):
    """largest integer dividing both a and b"""
    return math.gcd(a, b)
