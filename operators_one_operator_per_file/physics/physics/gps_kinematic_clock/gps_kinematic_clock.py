"""GPS kinematic clock   [(1/γ − 1) per day]

Category : Physics > Physics
Formula  : (1/γ − 1) · 86400 · 1000000   (microseconds per day by which a moving clock runs behind a clock at rest; the answer is negative)

Status   : ready to use - call compute(gamma)
"""
import math

NAME = 'GPS kinematic clock'
SYMBOL = '(1/γ − 1) per day'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = '(1/γ − 1) · 86400 · 1000000   (microseconds per day by which a moving clock runs behind a clock at rest; the answer is negative)'


def compute(gamma):
    """microseconds per day a moving clock loses: (1/γ − 1) · 86400 · 10⁶"""
    if gamma < 1:
        raise ValueError("a Lorentz factor is at least 1")
    return (1 / gamma - 1) * 86400 * 1000000
