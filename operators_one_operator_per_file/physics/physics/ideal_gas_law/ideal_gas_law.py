"""Ideal gas law   [PV = nRT]

Category : Physics > Physics
Formula  : P = n R T / V   (R = 8.314 J/(mol·K))

Status   : ready to use - call compute(n, T, V, R=8.314462618)
"""

NAME = 'Ideal gas law'
SYMBOL = 'PV = nRT'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'P = n R T / V   (R = 8.314 J/(mol·K))'


def compute(n, T, V, R=8.314462618):
    """P = n R T / V   (R = 8.314 J/(mol·K))"""
    return n * R * T / V
