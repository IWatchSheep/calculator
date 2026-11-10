"""Light deflection   [δ = 2 Rs / b]

Category : Physics > Physics
Formula  : δ = 4GM / (c² b) = 2 Rs / b   (the weak-field bend of a ray with closest approach b, in radians; only accurate when Rs/b is small; b ≤ (3√3/2) Rs falls into the mass)

Status   : ready to use - call compute(b, Rs)
"""
import math

NAME = 'Light deflection'
SYMBOL = 'δ = 2 Rs / b'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'δ = 4GM / (c² b) = 2 Rs / b   (the weak-field bend of a ray with closest approach b, in radians; only accurate when Rs/b is small; b ≤ (3√3/2) Rs falls into the mass)'


def compute(b, Rs):
    """δ = 2 Rs / b, radians"""
    if b <= 0:
        raise ValueError("a radius must be positive")
    if Rs <= 0:
        raise ValueError("the horizon radius must be positive")
    if b <= 1.5 * math.sqrt(3) * Rs:
        raise ValueError("the ray falls in; the small-angle formula does not apply")
    return 2 * Rs / b
