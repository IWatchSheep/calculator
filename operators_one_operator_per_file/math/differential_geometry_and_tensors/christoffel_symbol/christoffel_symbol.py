"""Christoffel symbol   [Γᵏᵢⱼ]

Category : Math > Differential geometry and tensors
Formula  : Γᵏᵢⱼ = ½ gᵏˡ (∂ᵢgⱼˡ + ∂ⱼgᵢˡ − ∂ˡgᵢⱼ)

Status   : reference only (no calculation is wired up yet)
"""

NAME = 'Christoffel symbol'
SYMBOL = 'Γᵏᵢⱼ'
CATEGORY = 'Math'
SUBCATEGORY = 'Differential geometry and tensors'
FORMULA = 'Γᵏᵢⱼ = ½ gᵏˡ (∂ᵢgⱼˡ + ∂ⱼgᵢˡ − ∂ˡgᵢⱼ)'


def compute(*args, **kwargs):
    """Reference only: see FORMULA above."""
    raise NotImplementedError('Christoffel symbol is reference-only for now; see FORMULA.')
