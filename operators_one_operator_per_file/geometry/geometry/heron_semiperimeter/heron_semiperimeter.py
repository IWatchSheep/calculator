"""Heron's formula: semi-perimeter   [s = (a+b+c)/2]

Category : Geometry > Geometry
Formula  : s = (a + b + c) / 2   (half the distance round the triangle)

Status   : ready to use - call compute(a, b, c)
"""

NAME = "Heron's formula: semi-perimeter"
SYMBOL = 's = (a+b+c)/2'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 's = (a + b + c) / 2   (half the distance round the triangle)'


def compute(a, b, c):
    """s = (a + b + c) / 2"""
    return (a + b + c) / 2
