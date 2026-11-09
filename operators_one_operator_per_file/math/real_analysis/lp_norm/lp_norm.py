"""Lp norm   [‖f‖ₚ]

Category : Math > Real analysis
Formula  : ‖f‖ₚ = (∫|f|ᵖ dx)^(1/p)   (numerical, Riemann sum)

Status   : ready to use - call compute(f, a, b, p=2, n=10000)
"""

NAME = 'Lp norm'
SYMBOL = '‖f‖ₚ'
CATEGORY = 'Math'
SUBCATEGORY = 'Real analysis'
FORMULA = '‖f‖ₚ = (∫|f|ᵖ dx)^(1/p)   (numerical, Riemann sum)'


def compute(f, a, b, p=2, n=10000):
    """‖f‖ₚ = (∫|f|ᵖ dx)^(1/p)   (numerical, Riemann sum)"""
    return (sum(abs(f(a + i * (b - a) / n)) ** p for i in range(n)) * (b - a) / n) ** (1 / p)
