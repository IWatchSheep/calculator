"""Infinite-well transition   [ΔE = (n₂² − n₁²) h² / (8 m L²)]

Category : Physics > Physics
Formula  : ΔE = (n₂² − n₁²) h² / (8 m L²)   (the photon energy when a particle in a one-dimensional box drops from level n₂ to the lower level n₁; h = 6.62607015e-34 J s)

Status   : ready to use - call compute(n2, n1, m, L, h=6.62607015e-34)
"""
NAME = 'Infinite-well transition'
SYMBOL = 'ΔE = (n₂² − n₁²) h² / (8 m L²)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'ΔE = (n₂² − n₁²) h² / (8 m L²)   (the photon energy when a particle in a one-dimensional box drops from level n₂ to the lower level n₁; h = 6.62607015e-34 J s)'


def compute(n2, n1, m, L, h=6.62607015e-34):
    """energy in joules released when the particle drops from n2 to n1"""
    for n in (n2, n1):
        if n < 1 or not float(n).is_integer():
            raise ValueError("a level must be a positive whole number")
    if n2 <= n1:
        raise ValueError("the upper level must be above the lower level")
    if m <= 0:
        raise ValueError("mass must be positive")
    if L <= 0:
        raise ValueError("a length must be positive")
    return (n2 ** 2 - n1 ** 2) * h ** 2 / (8 * m * L ** 2)
