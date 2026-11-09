"""Definite integral   [∫ₐᵇ]

Category : Math > Calculus
Formula  : ∫ₐᵇ f(x) dx   (numerical: Simpson's rule with n subintervals)

Status   : ready to use - call compute(f, a, b, n=1000)
"""

NAME = 'Definite integral'
SYMBOL = '∫ₐᵇ'
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = "∫ₐᵇ f(x) dx   (numerical: Simpson's rule with n subintervals)"


def compute(f, a, b, n=1000):
    """∫ₐᵇ f(x) dx   (numerical: Simpson's rule with n subintervals)"""
    if n % 2:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += (4 if i % 2 else 2) * f(a + i * h)
    return total * h / 3
