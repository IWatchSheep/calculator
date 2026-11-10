"""Oscillator ground-state variance   [⟨x²⟩ = ħ / (2 m ω)]

Category : Physics > Physics
Formula  : ⟨x²⟩ = ħ / (2 m ω)   (the mean of x is 0, so this is the spread of the ground state of a quantum harmonic oscillator, in square metres; ħ = 1.054571817e-34 J s unless another is passed)

Status   : ready to use - call compute(m, omega, hbar=1.054571817e-34)
"""
NAME = 'Oscillator ground-state variance'
SYMBOL = '⟨x²⟩ = ħ / (2 m ω)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = '⟨x²⟩ = ħ / (2 m ω)   (the mean of x is 0, so this is the spread of the ground state of a quantum harmonic oscillator, in square metres; ħ = 1.054571817e-34 J s unless another is passed)'


def compute(m, omega, hbar=1.054571817e-34):
    """variance in square metres"""
    if m <= 0:
        raise ValueError("mass must be positive")
    if omega <= 0:
        raise ValueError("the angular frequency must be positive")
    if hbar <= 0:
        raise ValueError("hbar must be positive")
    return hbar / (2 * m * omega)
