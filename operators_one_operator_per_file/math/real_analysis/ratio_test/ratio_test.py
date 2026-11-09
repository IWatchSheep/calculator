"""Ratio test   [L = |aₙ₊₁/aₙ|]

Category : Math > Real analysis
Formula  : L = lim |aₙ₊₁ / aₙ|;  converges if L < 1, diverges if L > 1

Status   : ready to use - call compute(a_n, a_next)
"""

NAME = 'Ratio test'
SYMBOL = 'L = |aₙ₊₁/aₙ|'
CATEGORY = 'Math'
SUBCATEGORY = 'Real analysis'
FORMULA = 'L = lim |aₙ₊₁ / aₙ|;  converges if L < 1, diverges if L > 1'


def compute(a_n, a_next):
    """L = lim |aₙ₊₁ / aₙ|;  converges if L < 1, diverges if L > 1"""
    return abs(a_next / a_n)
