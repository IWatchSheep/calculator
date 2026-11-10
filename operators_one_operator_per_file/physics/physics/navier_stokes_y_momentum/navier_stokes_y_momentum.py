"""Navier–Stokes: y momentum   [ρ Dv/Dt = −∂p/∂y + μ∇²v + f_y]

Category : Physics > Physics
Formula  : ρ(∂v/∂t + u ∂v/∂x + v ∂v/∂y + w ∂v/∂z) = −∂p/∂y + μ(∂²v/∂x² + ∂²v/∂y² + ∂²v/∂z²) + f_y   (incompressible flow)

Status   : reference only (no calculation is wired up yet)
"""

NAME = 'Navier–Stokes: y momentum'
SYMBOL = 'ρ Dv/Dt = −∂p/∂y + μ∇²v + f_y'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'ρ(∂v/∂t + u ∂v/∂x + v ∂v/∂y + w ∂v/∂z) = −∂p/∂y + μ(∂²v/∂x² + ∂²v/∂y² + ∂²v/∂z²) + f_y   (incompressible flow)'


def compute(*args, **kwargs):
    """Reference only: see FORMULA above."""
    raise NotImplementedError('Navier–Stokes: y momentum is reference-only for now; see FORMULA.')
