"""Polynomial ring   [R[x]]

Category : Math > Abstract algebra
Formula  : All polynomials a₀ + a₁x + … + aₙxⁿ with coefficients in R

Status   : reference only (no calculation is wired up yet)
"""

NAME = 'Polynomial ring'
SYMBOL = 'R[x]'
CATEGORY = 'Math'
SUBCATEGORY = 'Abstract algebra'
FORMULA = 'All polynomials a₀ + a₁x + … + aₙxⁿ with coefficients in R'


def compute(*args, **kwargs):
    """Reference only: see FORMULA above."""
    raise NotImplementedError('Polynomial ring is reference-only for now; see FORMULA.')
