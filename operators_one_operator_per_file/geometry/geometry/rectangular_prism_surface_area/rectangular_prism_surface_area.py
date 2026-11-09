"""Rectangular prism surface area   [2(lw+lh+wh)]

Category : Geometry > Geometry
Formula  : SA = 2(lw + lh + wh)

Status   : ready to use - call compute(l, w, h)
"""

NAME = 'Rectangular prism surface area'
SYMBOL = '2(lw+lh+wh)'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'SA = 2(lw + lh + wh)'


def compute(l, w, h):
    """SA = 2(lw + lh + wh)"""
    return 2 * (l * w + l * h + w * h)
