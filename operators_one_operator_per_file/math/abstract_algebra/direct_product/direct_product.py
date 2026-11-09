"""Direct product   [G × H]

Category : Math > Abstract algebra
Formula  : G × H = { (g, h) : g ∈ G, h ∈ H }

Status   : ready to use - call compute(G, H)
"""

NAME = 'Direct product'
SYMBOL = 'G × H'
CATEGORY = 'Math'
SUBCATEGORY = 'Abstract algebra'
FORMULA = 'G × H = { (g, h) : g ∈ G, h ∈ H }'


def compute(G, H):
    """G × H = { (g, h) : g ∈ G, h ∈ H }"""
    return [(g, h) for g in G for h in H]
