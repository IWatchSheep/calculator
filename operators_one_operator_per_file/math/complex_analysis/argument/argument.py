"""Argument   [arg(z)]

Category : Math > Complex analysis
Formula  : arg(a + bi) = atan2(b, a)

Status   : ready to use - call compute(z)
"""
import cmath

NAME = 'Argument'
SYMBOL = 'arg(z)'
CATEGORY = 'Math'
SUBCATEGORY = 'Complex analysis'
FORMULA = 'arg(a + bi) = atan2(b, a)'


def compute(z):
    """arg(a + bi) = atan2(b, a)"""
    return cmath.phase(z)
