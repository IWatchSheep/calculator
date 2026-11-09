"""Discriminant   [Δ]

Category : Math > Algebra
Formula  : Δ = b² − 4ac  (>0: two real roots, 0: one, <0: complex)

Status   : ready to use - call compute(a, b, c)
"""

NAME = 'Discriminant'
SYMBOL = 'Δ'
CATEGORY = 'Math'
SUBCATEGORY = 'Algebra'
FORMULA = 'Δ = b² − 4ac  (>0: two real roots, 0: one, <0: complex)'


def compute(a, b, c):
    """Δ = b² − 4ac  (>0: two real roots, 0: one, <0: complex)"""
    return b * b - 4 * a * c
