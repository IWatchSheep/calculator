"""Polygon interior angle sum   [(n−2)·180°]

Category : Geometry > Geometry
Formula  : sum of interior angles = (n − 2) × 180°

Status   : ready to use - call compute(n)
"""

NAME = 'Polygon interior angle sum'
SYMBOL = '(n−2)·180°'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'sum of interior angles = (n − 2) × 180°'


def compute(n):
    """sum of interior angles = (n − 2) × 180°"""
    return (n - 2) * 180
