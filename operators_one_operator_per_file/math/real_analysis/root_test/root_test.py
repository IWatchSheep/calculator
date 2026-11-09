"""Root test   [L = ⁿ√|aₙ|]

Category : Math > Real analysis
Formula  : L = lim ⁿ√|aₙ|;  converges if L < 1, diverges if L > 1

Status   : ready to use - call compute(a_n, n)
"""

NAME = 'Root test'
SYMBOL = 'L = ⁿ√|aₙ|'
CATEGORY = 'Math'
SUBCATEGORY = 'Real analysis'
FORMULA = 'L = lim ⁿ√|aₙ|;  converges if L < 1, diverges if L > 1'


def compute(a_n, n):
    """L = lim ⁿ√|aₙ|;  converges if L < 1, diverges if L > 1"""
    return abs(a_n) ** (1 / n)
