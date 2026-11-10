"""Navier–Stokes equation   [ρ(∂u/∂t + (u·∇)u) = −∇p + μ∇²u + f]

Category : Physics > Physics
Formula  : ρ(∂u/∂t + (u·∇)u) = −∇p + μ∇²u + f   (incompressible flow, ∇·u = 0)

Status   : reference only (no calculation is wired up yet)
"""

NAME = 'Navier–Stokes equation'
SYMBOL = 'ρ(∂u/∂t + (u·∇)u) = −∇p + μ∇²u + f'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'ρ(∂u/∂t + (u·∇)u) = −∇p + μ∇²u + f   (incompressible flow, ∇·u = 0)'


def compute(*args, **kwargs):
    """Reference only: see FORMULA above."""
    raise NotImplementedError('Navier–Stokes equation is reference-only for now; see FORMULA.')
