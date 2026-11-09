"""Coulomb's law   [F = k·q₁q₂/r²]

Category : Physics > Physics
Formula  : F = k q₁ q₂ / r²   (k = 8.988×10⁹ N·m²/C²)

Status   : ready to use - call compute(q1, q2, r, k=8.9875517923e9)
"""

NAME = "Coulomb's law"
SYMBOL = 'F = k·q₁q₂/r²'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'F = k q₁ q₂ / r²   (k = 8.988×10⁹ N·m²/C²)'


def compute(q1, q2, r, k=8.9875517923e9):
    """F = k q₁ q₂ / r²   (k = 8.988×10⁹ N·m²/C²)"""
    return k * q1 * q2 / r ** 2
