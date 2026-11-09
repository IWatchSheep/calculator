"""Exterior derivative   [d]

Category : Math > Differential geometry and tensors
Formula  : d(f dx) = df ∧ dx,  d² = 0

Status   : reference only (no calculation is wired up yet)
"""

NAME = 'Exterior derivative'
SYMBOL = 'd'
CATEGORY = 'Math'
SUBCATEGORY = 'Differential geometry and tensors'
FORMULA = 'd(f dx) = df ∧ dx,  d² = 0'


def compute(*args, **kwargs):
    """Reference only: see FORMULA above."""
    raise NotImplementedError('Exterior derivative is reference-only for now; see FORMULA.')
