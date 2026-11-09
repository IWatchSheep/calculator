"""Line integral   [∮]

Category : Math > Calculus
Formula  : ∮_C F · dr = ∫ₐᵇ F(r(t)) · r′(t) dt   (∮ when C is a closed curve)

Status   : ready to use - call compute(F, r, a, b)
"""

NAME = 'Line integral'
SYMBOL = '∮'
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = '∮_C F · dr = ∫ₐᵇ F(r(t)) · r′(t) dt   (∮ when C is a closed curve)'
import math
from operators_one_operator_per_file import _helpers as H


def compute(F, r, a, b):
    """∫ F(r(t)) · r′(t) dt from t = a to t = b   (F and r each give a list, e.g. r = [cos(t), sin(t)])"""
    def integrand(t, h=1e-6):
        pos = r(t)
        vel = [(p - m) / (2 * h) for p, m in zip(r(t + h), r(t - h))]
        return sum(fv * v for fv, v in zip(F(*pos), vel))
    return H.simpson(integrand, a, b, 1000)
