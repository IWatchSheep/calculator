"""Simpson's rule   [S]

Category : Math > Optimization and numerical methods
Formula  : ∫ₐᵇ f ≈ h/3 · (f₀ + 4f₁ + 2f₂ + … + fₙ),  n even

Status   : ready to use - call compute(f, a, b, n=1000)
"""

NAME = "Simpson's rule"
SYMBOL = 'S'
CATEGORY = 'Math'
SUBCATEGORY = 'Optimization and numerical methods'
FORMULA = '∫ₐᵇ f ≈ h/3 · (f₀ + 4f₁ + 2f₂ + … + fₙ),  n even'


def compute(f, a, b, n=1000):
    """∫ₐᵇ f ≈ h/3 · (f₀ + 4f₁ + 2f₂ + … + fₙ),  n even"""
    if n % 2:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += (4 if i % 2 else 2) * f(a + i * h)
    return total * h / 3
