"""Weight   [W = mg]

Category : Physics > Physics
Formula  : W = m g   (g = 9.81 m/s²)

Status   : ready to use - call compute(m, g=9.81)
"""

NAME = 'Weight'
SYMBOL = 'W = mg'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'W = m g   (g = 9.81 m/s²)'


def compute(m, g=9.81):
    """W = m g   (g = 9.81 m/s²)"""
    return m * g
