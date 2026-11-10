"""Oscillator level gap   [ΔE = ħ ω]

Category : Physics > Physics
Formula  : ΔE = ħ ω   (the energy between neighbouring levels of a quantum harmonic oscillator; it does not depend on n; ħ = 1.054571817e-34 J s unless another is passed)

Status   : ready to use - call compute(omega, hbar=1.054571817e-34)
"""
NAME = 'Oscillator level gap'
SYMBOL = 'ΔE = ħ ω'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'ΔE = ħ ω   (the energy between neighbouring levels of a quantum harmonic oscillator; it does not depend on n; ħ = 1.054571817e-34 J s unless another is passed)'


def compute(omega, hbar=1.054571817e-34):
    """energy gap in joules"""
    if omega <= 0:
        raise ValueError("the angular frequency must be positive")
    if hbar <= 0:
        raise ValueError("hbar must be positive")
    return hbar * omega
