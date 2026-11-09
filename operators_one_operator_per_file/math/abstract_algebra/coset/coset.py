"""Coset   [gH]

Category : Math > Abstract algebra
Formula  : gH = { g∘h : h ∈ H }

Status   : ready to use - call compute(g, H, op)
"""

NAME = 'Coset'
SYMBOL = 'gH'
CATEGORY = 'Math'
SUBCATEGORY = 'Abstract algebra'
FORMULA = 'gH = { g∘h : h ∈ H }'


def compute(g, H, op):
    """gH = { g∘h : h ∈ H }"""
    return {op(g, h) for h in H}
