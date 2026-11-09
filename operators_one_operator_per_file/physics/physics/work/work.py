"""Work   [W = Fd]

Category : Physics > Physics
Formula  : W = F d   (force parallel to displacement)

Status   : ready to use - call compute(F, d)
"""

NAME = 'Work'
SYMBOL = 'W = Fd'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'W = F d   (force parallel to displacement)'


def compute(F, d):
    """W = F d   (force parallel to displacement)"""
    return F * d
