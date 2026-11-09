"""De Moivre's theorem   [(r e^(iθ))ⁿ]

Category : Math > Complex analysis
Formula  : (r(cos θ + i sin θ))ⁿ = rⁿ(cos nθ + i sin nθ)

Status   : ready to use - call compute(r, theta, n)
"""
import cmath

NAME = "De Moivre's theorem"
SYMBOL = '(r e^(iθ))ⁿ'
CATEGORY = 'Math'
SUBCATEGORY = 'Complex analysis'
FORMULA = '(r(cos θ + i sin θ))ⁿ = rⁿ(cos nθ + i sin nθ)'


def compute(r, theta, n):
    """(r(cos θ + i sin θ))ⁿ = rⁿ(cos nθ + i sin nθ)"""
    return cmath.rect(r ** n, n * theta)
