"""Gravitational-wave strain   [h = 4 (G Mc)^(5/3) (π f)^(2/3) / (c⁴ d)]

Category : Physics > Physics
Formula  : h = 4 (G Mc)^(5/3) (π f)^(2/3) / (c⁴ d)   (leading-order amplitude of a face-on circular binary at distance d; f is the wave frequency, twice the orbital frequency; G = 6.674e-11, c = 299792458)

Status   : ready to use - call compute(chirp_mass, f_gw, distance, G=6.674e-11, c=299792458)
"""
import math

NAME = 'Gravitational-wave strain'
SYMBOL = 'h = 4 (G Mc)^(5/3) (π f)^(2/3) / (c⁴ d)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'h = 4 (G Mc)^(5/3) (π f)^(2/3) / (c⁴ d)   (leading-order amplitude of a face-on circular binary at distance d; f is the wave frequency, twice the orbital frequency; G = 6.674e-11, c = 299792458)'


def compute(chirp_mass, f_gw, distance, G=6.674e-11, c=299792458):
    """h = 4 (G Mc)^(5/3) (π f)^(2/3) / (c⁴ d), dimensionless"""
    if chirp_mass <= 0:
        raise ValueError("mass must be positive")
    if distance <= 0:
        raise ValueError("a distance must be positive")
    if f_gw < 0:
        raise ValueError("a frequency cannot be negative")
    return 4 * (G * chirp_mass) ** (5 / 3) * (math.pi * f_gw) ** (2 / 3) / (c ** 4 * distance)
