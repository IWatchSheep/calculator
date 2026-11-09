"""Mobius transformation   [(az+b)/(cz+d)]

Category : Math > Complex analysis
Formula  : f(z) = (az + b) / (cz + d),  ad − bc ≠ 0

Status   : ready to use - call compute(a, b, c, d, z)
"""

NAME = 'Mobius transformation'
SYMBOL = '(az+b)/(cz+d)'
CATEGORY = 'Math'
SUBCATEGORY = 'Complex analysis'
FORMULA = 'f(z) = (az + b) / (cz + d),  ad − bc ≠ 0'


def compute(a, b, c, d, z):
    """f(z) = (az + b) / (cz + d),  ad − bc ≠ 0"""
    return (a * z + b) / (c * z + d)
