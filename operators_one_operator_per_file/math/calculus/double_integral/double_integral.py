"""Double integral   [∬]

Category : Math > Calculus
Formula  : ∬_R f(x, y) dA = ∫∫ f(x, y) dy dx over a region R

Status   : ready to use - call compute(f, x0, x1, y0, y1)
"""

NAME = 'Double integral'
SYMBOL = '∬'
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = '∬_R f(x, y) dA = ∫∫ f(x, y) dy dx over a region R'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, x0, x1, y0, y1):
    """∬ f(x, y) dy dx over the rectangle x0 ≤ x ≤ x1, y0 ≤ y ≤ y1  (Simpson's rule)"""
    return H.simpson(lambda x: H.simpson(lambda y: f(x, y), y0, y1, 100), x0, x1, 100)
