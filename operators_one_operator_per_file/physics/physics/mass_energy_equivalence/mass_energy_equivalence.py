"""Mass-energy equivalence   [E = mc²]

Category : Physics > Physics
Formula  : E = m c²   (c = 299 792 458 m/s)

Status   : ready to use - call compute(m, c=299792458)
"""

NAME = 'Mass-energy equivalence'
SYMBOL = 'E = mc²'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'E = m c²   (c = 299 792 458 m/s)'


def compute(m, c=299792458):
    """E = m c²   (c = 299 792 458 m/s)"""
    return m * c ** 2
