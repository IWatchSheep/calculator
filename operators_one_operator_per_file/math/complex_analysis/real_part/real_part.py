"""Real part   [Re(z)]

Category : Math > Complex analysis
Formula  : Re(a + bi) = a

Status   : ready to use - call compute(z)
"""

NAME = 'Real part'
SYMBOL = 'Re(z)'
CATEGORY = 'Math'
SUBCATEGORY = 'Complex analysis'
FORMULA = 'Re(a + bi) = a'


def compute(z):
    """Re(a + bi) = a"""
    return complex(z).real
