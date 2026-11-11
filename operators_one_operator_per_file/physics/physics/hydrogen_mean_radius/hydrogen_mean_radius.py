"""Hydrogen mean radius   [⟨r⟩ = (a₀ / (2 Z)) [3 n² − l(l+1)]]

Category : Physics > Physics
Formula  : ⟨r⟩ = (a₀ / (2 Z)) [3 n² − l(l+1)]   (the average distance of the electron from the nucleus in hydrogen or a one-electron ion, in metres; a₀ = 5.29177210903e-11 m is the hydrogen Bohr radius; it does not depend on the magnetic number)

Status   : ready to use - call compute(n, l, Z, a0=5.29177210903e-11)
"""
NAME = 'Hydrogen mean radius'
SYMBOL = '⟨r⟩ = (a₀ / (2 Z)) [3 n² − l(l+1)]'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = '⟨r⟩ = (a₀ / (2 Z)) [3 n² − l(l+1)]   (the average distance of the electron from the nucleus in hydrogen or a one-electron ion, in metres; a₀ = 5.29177210903e-11 m is the hydrogen Bohr radius; it does not depend on the magnetic number)'


def compute(n, l, Z, a0=5.29177210903e-11):
    """mean radius in metres"""
    if n < 1 or not float(n).is_integer():
        raise ValueError("a level must be a positive whole number")
    if Z < 1 or not float(Z).is_integer():
        raise ValueError("the atomic number must be a positive whole number")
    if l < 0 or l > n - 1 or not float(l).is_integer():
        raise ValueError("the angular momentum must be a whole number from 0 up to n - 1")
    return a0 / (2 * Z) * (3 * n ** 2 - l * (l + 1))
