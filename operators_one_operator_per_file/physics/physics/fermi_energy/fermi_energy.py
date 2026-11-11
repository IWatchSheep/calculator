"""Fermi energy   [E_F = (ħ² / 2 m) (3 π² n)^(2/3)]

Category : Physics > Physics
Formula  : E_F = (ħ² / 2 m) (3 π² n)^(2/3)   (the Fermi energy in joules of a three-dimensional free-electron gas at zero temperature; n is the number of electrons per cubic metre; ħ = 1.054571817e-34 J s unless another is passed; not a band structure)

Status   : ready to use - call compute(n, m, hbar=1.054571817e-34)
"""
import math

NAME = 'Fermi energy'
SYMBOL = 'E_F = (ħ² / 2 m) (3 π² n)^(2/3)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'E_F = (ħ² / 2 m) (3 π² n)^(2/3)   (the Fermi energy in joules of a three-dimensional free-electron gas at zero temperature; n is the number of electrons per cubic metre; ħ = 1.054571817e-34 J s unless another is passed; not a band structure)'


def compute(n, m, hbar=1.054571817e-34):
    """Fermi energy in joules"""
    if n <= 0:
        raise ValueError("the density must be positive")
    if m <= 0:
        raise ValueError("mass must be positive")
    if hbar <= 0:
        raise ValueError("hbar must be positive")
    return hbar ** 2 / (2 * m) * (3 * math.pi ** 2 * n) ** (2 / 3)
