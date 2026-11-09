"""Bohr energy level (hydrogen-like atom)   [Eₙ = −13.6 Z²/n² eV]

Category : Physics > Physics
Formula  : Eₙ = −13.605693 eV × Z² / n²   (energy in electron-volts)

Status   : ready to use - call compute(n, Z)
"""
import math

NAME = 'Bohr energy level (hydrogen-like atom)'
SYMBOL = 'Eₙ = −13.6 Z²/n² eV'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'Eₙ = −13.605693 eV × Z² / n²   (energy in electron-volts)'


def compute(n, Z=1):
    """Eₙ = −13.605693 eV × Z² / n²   (energy in electron-volts)"""
    return -13.605693122994 * Z ** 2 / n ** 2
