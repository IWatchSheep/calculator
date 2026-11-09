"""Discrete Fourier transform   [F{x}]

Category : Math > Transforms and differential equations
Formula  : Xₖ = Σₙ xₙ · e^(−2πi·kn/N)

Status   : ready to use - call compute(x)
"""
import cmath

NAME = 'Discrete Fourier transform'
SYMBOL = 'F{x}'
CATEGORY = 'Math'
SUBCATEGORY = 'Transforms and differential equations'
FORMULA = 'Xₖ = Σₙ xₙ · e^(−2πi·kn/N)'


def compute(x):
    """Xₖ = Σₙ xₙ · e^(−2πi·kn/N)"""
    return [sum(x[n] * cmath.exp(-2j * cmath.pi * k * n / len(x)) for n in range(len(x))) for k in range(len(x))]
