"""Navier–Stokes: z momentum   [ρ Dw/Dt = −∂p/∂z + μ∇²w + f_z]

Category : Physics > Physics
Formula  : ρ(∂w/∂t + u ∂w/∂x + v ∂w/∂y + w ∂w/∂z) = −∂p/∂z + μ(∂²w/∂x² + ∂²w/∂y² + ∂²w/∂z²) + f_z   (incompressible flow)

Status   : reference only (no calculation is wired up yet)
"""

NAME = 'Navier–Stokes: z momentum'
SYMBOL = 'ρ Dw/Dt = −∂p/∂z + μ∇²w + f_z'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'ρ(∂w/∂t + u ∂w/∂x + v ∂w/∂y + w ∂w/∂z) = −∂p/∂z + μ(∂²w/∂x² + ∂²w/∂y² + ∂²w/∂z²) + f_z   (incompressible flow)'


def compute(*args, **kwargs):
    """Reference only: see FORMULA above."""
    raise NotImplementedError('Navier–Stokes: z momentum is reference-only for now; see FORMULA.')
