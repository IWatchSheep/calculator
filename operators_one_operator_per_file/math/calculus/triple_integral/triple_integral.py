"""Triple integral   [∭]

Category : Math > Calculus
Formula  : ∭_V f(x, y, z) dV = ∫∫∫ f(x, y, z) dz dy dx over a volume V

Status   : ready to use - call compute(f, x0, x1, y0, y1, z0, z1)
"""

NAME = 'Triple integral'
SYMBOL = '∭'
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = '∭_V f(x, y, z) dV = ∫∫∫ f(x, y, z) dz dy dx over a volume V'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, x0, x1, y0, y1, z0, z1):
    """∭ f(x, y, z) dz dy dx over a box  (Simpson's rule)"""
    return H.simpson(lambda x: H.simpson(lambda y: H.simpson(lambda z: f(x, y, z), z0, z1, 24), y0, y1, 24), x0, x1, 24)
