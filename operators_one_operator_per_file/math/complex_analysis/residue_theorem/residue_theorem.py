"""Residue theorem   [2πi Σ Res]

Category : Math > Complex analysis
Formula  : ∮_C f(z) dz = 2πi Σ Res(f, aₖ) over poles aₖ inside C

Status   : ready to use - call compute(f, center, radius)
"""

NAME = 'Residue theorem'
SYMBOL = '2πi Σ Res'
CATEGORY = 'Math'
SUBCATEGORY = 'Complex analysis'
FORMULA = '∮_C f(z) dz = 2πi Σ Res(f, aₖ) over poles aₖ inside C'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, center, radius):
    """∮ f(z) dz = 2πi · (sum of the residues inside the circle) — computed round the circle |z − center| = radius"""
    return H.circle_integral(f, center, radius)
