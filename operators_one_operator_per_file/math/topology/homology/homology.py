"""Homology   [Hₙ(X)]

Category : Math > Topology
Formula  : Hₙ = ker ∂ₙ / im ∂ₙ₊₁

Status   : reference only (no calculation is wired up yet)
"""

NAME = 'Homology'
SYMBOL = 'Hₙ(X)'
CATEGORY = 'Math'
SUBCATEGORY = 'Topology'
FORMULA = 'Hₙ = ker ∂ₙ / im ∂ₙ₊₁'


def compute(*args, **kwargs):
    """Reference only: see FORMULA above."""
    raise NotImplementedError('Homology is reference-only for now; see FORMULA.')
