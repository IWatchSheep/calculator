"""Gravitation   [F = G·m₁m₂/r²]

Category : Physics > Physics
Formula  : F = G m₁ m₂ / r²   (G = 6.674×10⁻¹¹ N·m²/kg²)

Status   : ready to use - call compute(m1, m2, r, G=6.674e-11)
"""

NAME = 'Gravitation'
SYMBOL = 'F = G·m₁m₂/r²'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'F = G m₁ m₂ / r²   (G = 6.674×10⁻¹¹ N·m²/kg²)'


def compute(m1, m2, r, G=6.674e-11):
    """F = G m₁ m₂ / r²   (G = 6.674×10⁻¹¹ N·m²/kg²)"""
    return G * m1 * m2 / r ** 2
