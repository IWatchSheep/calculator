"""Inverse Laplace transform   [L⁻¹{F}]

Category : Math > Transforms and differential equations
Formula  : f(t) = (1 / 2πi) ∫ F(s) e^(st) ds

Status   : reference only (no calculation is wired up yet)
"""

NAME = 'Inverse Laplace transform'
SYMBOL = 'L⁻¹{F}'
CATEGORY = 'Math'
SUBCATEGORY = 'Transforms and differential equations'
FORMULA = 'f(t) = (1 / 2πi) ∫ F(s) e^(st) ds'


def compute(*args, **kwargs):
    """Reference only: see FORMULA above."""
    raise NotImplementedError('Inverse Laplace transform is reference-only for now; see FORMULA.')
