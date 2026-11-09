"""Regular polygon area   [½·p·a]

Category : Geometry > Geometry
Formula  : A = ½ · perimeter · apothem

Status   : ready to use - call compute(perimeter, apothem)
"""

NAME = 'Regular polygon area'
SYMBOL = '½·p·a'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'A = ½ · perimeter · apothem'


def compute(perimeter, apothem):
    """A = ½ · perimeter · apothem"""
    return 0.5 * perimeter * apothem
