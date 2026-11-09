"""Heat   [Q = mcΔT]

Category : Physics > Physics
Formula  : Q = m c ΔT

Status   : ready to use - call compute(m, c, delta_T)
"""

NAME = 'Heat'
SYMBOL = 'Q = mcΔT'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'Q = m c ΔT'


def compute(m, c, delta_T):
    """Q = m c ΔT"""
    return m * c * delta_T
