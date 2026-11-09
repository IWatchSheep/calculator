"""Imaginary part   [Im(z)]

Category : Math > Complex analysis
Formula  : Im(a + bi) = b

Status   : ready to use - call compute(z)
"""

NAME = 'Imaginary part'
SYMBOL = 'Im(z)'
CATEGORY = 'Math'
SUBCATEGORY = 'Complex analysis'
FORMULA = 'Im(a + bi) = b'


def compute(z):
    """Im(a + bi) = b"""
    return complex(z).imag
