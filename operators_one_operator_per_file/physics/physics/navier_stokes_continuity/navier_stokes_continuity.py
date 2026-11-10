"""Navier–Stokes: continuity (incompressible)   [∇·u = 0]

Category : Physics > Physics
Formula  : ∂u/∂x + ∂v/∂y + ∂w/∂z = 0   (incompressible flow)

Status   : reference only (no calculation is wired up yet)
"""

NAME = 'Navier–Stokes: continuity (incompressible)'
SYMBOL = '∇·u = 0'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = '∂u/∂x + ∂v/∂y + ∂w/∂z = 0   (incompressible flow)'


def compute(*args, **kwargs):
    """Reference only: see FORMULA above."""
    raise NotImplementedError('Navier–Stokes: continuity (incompressible) is reference-only for now; see FORMULA.')
