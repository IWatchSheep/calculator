"""Gaussian curvature   [K]

Category : Math > Differential geometry and tensors
Formula  : K = κ₁ · κ₂  (product of the principal curvatures)

Status   : ready to use - call compute(k1, k2)
"""

NAME = 'Gaussian curvature'
SYMBOL = 'K'
CATEGORY = 'Math'
SUBCATEGORY = 'Differential geometry and tensors'
FORMULA = 'K = κ₁ · κ₂  (product of the principal curvatures)'


def compute(k1, k2):
    """K = κ₁ · κ₂  (product of the principal curvatures)"""
    return k1 * k2
