"""Pyramid volume   [⅓Bh]

Category : Geometry > Geometry
Formula  : V = ⅓ · base area · height

Status   : ready to use - call compute(base_area, h)
"""

NAME = 'Pyramid volume'
SYMBOL = '⅓Bh'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'V = ⅓ · base area · height'


def compute(base_area, h):
    """V = ⅓ · base area · height"""
    return base_area * h / 3
