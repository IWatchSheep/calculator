"""Z-transform   [X(z)]

Category : Math > Transforms and differential equations
Formula  : X(z) = Σₙ x[n] · z⁻ⁿ

Status   : ready to use - call compute(x, z)
"""

NAME = 'Z-transform'
SYMBOL = 'X(z)'
CATEGORY = 'Math'
SUBCATEGORY = 'Transforms and differential equations'
FORMULA = 'X(z) = Σₙ x[n] · z⁻ⁿ'


def compute(x, z):
    """X(z) = Σₙ x[n] · z⁻ⁿ"""
    return sum(x[n] * z ** (-n) for n in range(len(x)))
