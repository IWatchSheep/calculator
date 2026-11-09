"""Quantum harmonic oscillator   [Eₙ = ħω(n + ½)]

Category : Physics > Physics
Formula  : Eₙ = ħ ω (n + ½)   (ω in rad/s)

Status   : ready to use - call compute(n, omega, hbar)
"""
import math

NAME = 'Quantum harmonic oscillator'
SYMBOL = 'Eₙ = ħω(n + ½)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'Eₙ = ħ ω (n + ½)   (ω in rad/s)'


def compute(n, omega, hbar=1.054571817e-34):
    """Eₙ = ħ ω (n + ½)   (ω in rad/s)"""
    return hbar * omega * (n + 0.5)
