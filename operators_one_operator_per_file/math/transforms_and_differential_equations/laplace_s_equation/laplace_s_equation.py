"""Laplace's equation   [∇²u = 0]

Category : Math > Transforms and differential equations
Formula  : ∂²u/∂x² + ∂²u/∂y² + ∂²u/∂z² = 0

Status   : reference only (no calculation is wired up yet)
"""

NAME = "Laplace's equation"
SYMBOL = '∇²u = 0'
CATEGORY = 'Math'
SUBCATEGORY = 'Transforms and differential equations'
FORMULA = '∂²u/∂x² + ∂²u/∂y² + ∂²u/∂z² = 0'


def compute(*args, **kwargs):
    """Reference only: see FORMULA above."""
    raise NotImplementedError("Laplace's equation is reference-only for now; see FORMULA.")
