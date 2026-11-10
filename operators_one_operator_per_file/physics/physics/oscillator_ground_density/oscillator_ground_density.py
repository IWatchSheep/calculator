"""Oscillator ground-state density   [|ψ₀|² = √(m ω / (π ħ)) exp(−m ω x² / ħ)]

Category : Physics > Physics
Formula  : |ψ₀|² = √(m ω / (π ħ)) exp(−m ω x² / ħ)   (the probability per metre of finding the particle at x in the ground state of a quantum harmonic oscillator; ħ = 1.054571817e-34 J s unless another is passed)

Status   : ready to use - call compute(m, omega, x, hbar=1.054571817e-34)
"""
import math

NAME = 'Oscillator ground-state density'
SYMBOL = '|ψ₀|² = √(m ω / (π ħ)) exp(−m ω x² / ħ)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = '|ψ₀|² = √(m ω / (π ħ)) exp(−m ω x² / ħ)   (the probability per metre of finding the particle at x in the ground state of a quantum harmonic oscillator; ħ = 1.054571817e-34 J s unless another is passed)'


def compute(m, omega, x, hbar=1.054571817e-34):
    """probability per metre"""
    if m <= 0:
        raise ValueError("mass must be positive")
    if omega <= 0:
        raise ValueError("the angular frequency must be positive")
    if hbar <= 0:
        raise ValueError("hbar must be positive")
    return math.sqrt(m * omega / (math.pi * hbar)) * math.exp(-m * omega * x ** 2 / hbar)
