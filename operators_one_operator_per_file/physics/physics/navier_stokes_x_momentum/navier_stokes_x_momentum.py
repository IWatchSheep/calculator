"""Navier–Stokes: x momentum   [ρ Du/Dt = −∂p/∂x + μ∇²u + fₓ]

Category : Physics > Physics
Formula  : ρ(∂u/∂t + u ∂u/∂x + v ∂u/∂y + w ∂u/∂z) = −∂p/∂x + μ(∂²u/∂x² + ∂²u/∂y² + ∂²u/∂z²) + f_x   (incompressible flow)

Status   : reference only (no calculation is wired up yet)
"""

NAME = 'Navier–Stokes: x momentum'
SYMBOL = 'ρ Du/Dt = −∂p/∂x + μ∇²u + fₓ'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'ρ(∂u/∂t + u ∂u/∂x + v ∂u/∂y + w ∂u/∂z) = −∂p/∂x + μ(∂²u/∂x² + ∂²u/∂y² + ∂²u/∂z²) + f_x   (incompressible flow)'


def compute(*args, **kwargs):
    """Reference only: see FORMULA above."""
    raise NotImplementedError('Navier–Stokes: x momentum is reference-only for now; see FORMULA.')
