"""Burnside's lemma   [|X/G|]

Category : Math > Graph theory and combinatorics
Formula  : Number of orbits = (1/|G|) Σ_g |Fix(g)|

Status   : ready to use - call compute(fixed_counts)
"""

NAME = "Burnside's lemma"
SYMBOL = '|X/G|'
CATEGORY = 'Math'
SUBCATEGORY = 'Graph theory and combinatorics'
FORMULA = 'Number of orbits = (1/|G|) Σ_g |Fix(g)|'


def compute(fixed_counts):
    """Number of orbits = (1/|G|) Σ_g |Fix(g)|"""
    return sum(fixed_counts) / len(fixed_counts)
