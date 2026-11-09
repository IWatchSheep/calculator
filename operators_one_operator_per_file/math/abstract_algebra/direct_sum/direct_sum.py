"""Direct sum   [⊕]

Category : Math > Abstract algebra
Formula  : A ⊕ B = { (a, b) : a ∈ A, b ∈ B } with component-wise operations; dim(A ⊕ B) = dim A + dim B

Status   : reference only (no calculation is wired up yet)
"""

NAME = 'Direct sum'
SYMBOL = '⊕'
CATEGORY = 'Math'
SUBCATEGORY = 'Abstract algebra'
FORMULA = 'A ⊕ B = { (a, b) : a ∈ A, b ∈ B } with component-wise operations; dim(A ⊕ B) = dim A + dim B'


def compute(*args, **kwargs):
    """Reference only: see FORMULA above."""
    raise NotImplementedError('Direct sum is reference-only for now; see FORMULA.')
