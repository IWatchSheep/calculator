"""Heat equation   [uₜ = α uₓₓ]

Category : Math > Transforms and differential equations
Formula  : ∂u/∂t = α ∂²u/∂x²

Status   : reference only (no calculation is wired up yet)
"""

NAME = 'Heat equation'
SYMBOL = 'uₜ = α uₓₓ'
CATEGORY = 'Math'
SUBCATEGORY = 'Transforms and differential equations'
FORMULA = '∂u/∂t = α ∂²u/∂x²'


def compute(*args, **kwargs):
    """Reference only: see FORMULA above."""
    raise NotImplementedError('Heat equation is reference-only for now; see FORMULA.')
