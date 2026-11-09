"""Inverse discrete Fourier transform   [F⁻¹{X}]

Category : Math > Transforms and differential equations
Formula  : xₙ = (1/N) Σₖ Xₖ · e^(2πi·kn/N)

Status   : ready to use - call compute(X)
"""
import cmath

NAME = 'Inverse discrete Fourier transform'
SYMBOL = 'F⁻¹{X}'
CATEGORY = 'Math'
SUBCATEGORY = 'Transforms and differential equations'
FORMULA = 'xₙ = (1/N) Σₖ Xₖ · e^(2πi·kn/N)'


def compute(X):
    """xₙ = (1/N) Σₖ Xₖ · e^(2πi·kn/N)"""
    return [sum(X[k] * cmath.exp(2j * cmath.pi * k * n / len(X)) for k in range(len(X))) / len(X) for n in range(len(X))]
