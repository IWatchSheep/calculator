"""Bohr radius   [a = a₀ / Z]

Category : Physics > Physics
Formula  : a = a₀ / Z   (a₀ = 5.29177210903e-11 m, the hydrogen Bohr radius; a nucleus of charge Z pulls it in to a₀/Z)

Status   : ready to use - call compute(Z, a0=5.29177210903e-11)
"""
NAME = 'Bohr radius'
SYMBOL = 'a = a₀ / Z'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'a = a₀ / Z   (a₀ = 5.29177210903e-11 m, the hydrogen Bohr radius; a nucleus of charge Z pulls it in to a₀/Z)'


def compute(Z, a0=5.29177210903e-11):
    """radius in metres"""
    if Z < 1 or not float(Z).is_integer():
        raise ValueError("the atomic number must be a positive whole number")
    return a0 / Z
