"""GPS gravitational clock   [GM (1/R − 1/r) / c² per day]

Category : Physics > Physics
Formula  : GM (1/R − 1/r) / c² · 86400 · 10⁶   (microseconds per day by which a clock at radius r runs ahead of a clock at radius R; GM = 3.986004418e14 m³/s², c = 299792458 m/s)

Status   : ready to use - call compute(ground_radius, satellite_radius)
"""
import math

NAME = 'GPS gravitational clock'
SYMBOL = 'GM (1/R − 1/r) / c² per day'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'GM (1/R − 1/r) / c² · 86400 · 10⁶   (microseconds per day by which a clock at radius r runs ahead of a clock at radius R; GM = 3.986004418e14 m³/s², c = 299792458 m/s)'


def compute(ground_radius, satellite_radius):
    """microseconds per day a clock at the satellite radius gains on the ground"""
    if ground_radius <= 0 or satellite_radius <= 0:
        raise ValueError("a radius must be positive")
    if satellite_radius <= ground_radius:
        raise ValueError("the satellite must be above the ground")
    GM = 3.986004418e14
    c = 299792458
    return GM * (1 / ground_radius - 1 / satellite_radius) / (c * c) * 86400 * 1000000
