"""Centre of mass   [Σ m x / Σ m]

Category : Physics > Physics
Formula  : [x, y, z] = Σ mᵢ pᵢ / Σ mᵢ   (each position is x, y, z in metres)

Status   : ready to use - call compute(masses, positions)
"""
import math

NAME = 'Centre of mass'
SYMBOL = 'Σ m x / Σ m'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = '[x, y, z] = Σ mᵢ pᵢ / Σ mᵢ   (each position is x, y, z in metres)'


def compute(masses, positions):
    """the centre of mass [x, y, z] of point masses"""
    if len(masses) != len(positions):
        raise ValueError("each mass needs a position")
    if any(len(p) != 3 for p in positions):
        raise ValueError("a position has 3 numbers: x, y, z")
    if any(m < 0 for m in masses):
        raise ValueError("mass cannot be negative")
    if len(masses) == 0:
        raise ValueError("there are no points")
    total = sum(masses)
    if total == 0:
        raise ValueError("the total mass is zero")
    return [sum(m * p[k] for m, p in zip(masses, positions)) / total for k in range(3)]
