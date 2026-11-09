"""Prime check   [prime?]

Category : Math > Discrete and number theory
Formula  : n is prime if n > 1 and has no divisor other than 1 and n

Status   : ready to use - call compute(n)
"""

NAME = 'Prime check'
SYMBOL = 'prime?'
CATEGORY = 'Math'
SUBCATEGORY = 'Discrete and number theory'
FORMULA = 'n is prime if n > 1 and has no divisor other than 1 and n'


def compute(n):
    """n is prime if n > 1 and has no divisor other than 1 and n"""
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
