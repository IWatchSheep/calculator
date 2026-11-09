"""Prime factorization   [n = p₁·p₂·…]

Category : Math > Discrete and number theory
Formula  : every integer > 1 is a product of primes

Status   : ready to use - call compute(n)
"""

NAME = 'Prime factorization'
SYMBOL = 'n = p₁·p₂·…'
CATEGORY = 'Math'
SUBCATEGORY = 'Discrete and number theory'
FORMULA = 'every integer > 1 is a product of primes'


def compute(n):
    """every integer > 1 is a product of primes"""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors
