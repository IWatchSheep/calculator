"""Two-argument arctangent   [atan2]

Category : Math > Trigonometry
Formula  : atan2(y, x) = angle of the point (x, y) from the +x axis

Status   : ready to use - call compute(y, x)
"""
import math

NAME = 'Two-argument arctangent'
SYMBOL = 'atan2'
CATEGORY = 'Math'
SUBCATEGORY = 'Trigonometry'
FORMULA = 'atan2(y, x) = angle of the point (x, y) from the +x axis'


def compute(y, x):
    """atan2(y, x) = angle of the point (x, y) from the +x axis"""
    return math.atan2(y, x)
