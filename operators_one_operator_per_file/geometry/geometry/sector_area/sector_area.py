"""Sector area   [½r²θ]

Category : Geometry > Geometry
Formula  : A = ½ r² θ   (θ in radians)

Status   : ready to use - call compute(r, theta)
"""

NAME = 'Sector area'
SYMBOL = '½r²θ'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 'A = ½ r² θ   (θ in radians)'


def compute(r, theta):
    """A = ½ r² θ   (θ in radians)"""
    return 0.5 * r ** 2 * theta
