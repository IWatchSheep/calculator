"""Arc length   [rθ]

Category : Geometry > Geometry
Formula  : s = r θ   (θ in radians)

Status   : ready to use - call compute(r, theta)
"""

NAME = 'Arc length'
SYMBOL = 'rθ'
CATEGORY = 'Geometry'
SUBCATEGORY = 'Geometry'
FORMULA = 's = r θ   (θ in radians)'


def compute(r, theta):
    """s = r θ   (θ in radians)"""
    return r * theta
