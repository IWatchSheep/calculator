"""Second derivative   [d²/dx²]

Category : Math > Calculus
Formula  : f″(x) ≈ (f(x+h) − 2f(x) + f(x−h)) / h²

Status   : ready to use - call compute(f, x, h=1e-4)
"""

NAME = 'Second derivative'
SYMBOL = 'd²/dx²'
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = 'f″(x) ≈ (f(x+h) − 2f(x) + f(x−h)) / h²'


def compute(f, x, h=1e-4):
    """f″(x) ≈ (f(x+h) − 2f(x) + f(x−h)) / h²"""
    return (f(x + h) - 2 * f(x) + f(x - h)) / h ** 2
