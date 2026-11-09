"""Inner product   [⟨x, y⟩]

Category : Math > Real analysis
Formula  : ⟨x, y⟩ = Σ xᵢyᵢ   (real vectors)

Status   : ready to use - call compute(x, y)
"""

NAME = 'Inner product'
SYMBOL = '⟨x, y⟩'
CATEGORY = 'Math'
SUBCATEGORY = 'Real analysis'
FORMULA = '⟨x, y⟩ = Σ xᵢyᵢ   (real vectors)'


def compute(x, y):
    """⟨x, y⟩ = Σ xᵢyᵢ   (real vectors)"""
    return sum(a * b for a, b in zip(x, y))
