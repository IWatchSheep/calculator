"""Open ball   [B(x, r)]

Category : Math > Topology
Formula  : B(x, r) = { y : d(x, y) < r };  returns True if y is in the ball

Status   : ready to use - call compute(d, x, y, r)
"""

NAME = 'Open ball'
SYMBOL = 'B(x, r)'
CATEGORY = 'Math'
SUBCATEGORY = 'Topology'
FORMULA = 'B(x, r) = { y : d(x, y) < r };  returns True if y is in the ball'


def compute(d, x, y, r):
    """B(x, r) = { y : d(x, y) < r };  returns True if y is in the ball"""
    return d(x, y) < r
