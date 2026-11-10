"""TOV pressure step   [ΔP = (dP/dr) Δr, one shell of a static spherical star]

Category : Physics > Physics
Formula  : ΔP = −(G M ρ / r²) (1 + P/(ρ c²)) (1 + 4π r³ P / (M c²)) / (1 − 2GM/(r c²)) Δr   (one thin shell of the Tolman–Oppenheimer–Volkoff equation; M is the mass already inside r; G = 6.674e-11, c = 299792458)

Status   : ready to use - call compute(r, dr, M, rho, P, G=6.674e-11, c=299792458)
"""
import math

NAME = 'TOV pressure step'
SYMBOL = 'one shell of dP/dr'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'ΔP = −(G M ρ / r²) (1 + P/(ρ c²)) (1 + 4π r³ P / (M c²)) / (1 − 2GM/(r c²)) Δr   (the pressure change across one thin shell of a static spherical star, Tolman–Oppenheimer–Volkoff; M is the mass already inside r; G = 6.674e-11, c = 299792458)'


def compute(r, dr, M, rho, P, G=6.674e-11, c=299792458):
    """pressure change in pascals across a shell of thickness dr (negative for a normal star)"""
    if r <= 0:
        raise ValueError("a radius must be positive")
    if dr <= 0:
        raise ValueError("the shell thickness must be positive")
    if M <= 0:
        raise ValueError("mass must be positive")
    if rho <= 0:
        raise ValueError("density must be positive")
    if P < 0:
        raise ValueError("pressure cannot be negative")
    if 2 * G * M / (r * c ** 2) >= 1:
        raise ValueError("r is not outside the horizon")
    return -(G * M * rho / r ** 2) * (1 + P / (rho * c ** 2)) * (1 + 4 * math.pi * r ** 3 * P / (M * c ** 2)) / (1 - 2 * G * M / (r * c ** 2)) * dr
