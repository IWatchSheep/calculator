"""Chirp mass   [(m1 m2)^(3/5) / (m1 + m2)^(1/5)]

Category : Physics > Physics
Formula  : Mc = (m1 m2)^(3/5) / (m1 + m2)^(1/5)   (the mass combination that sets the leading gravitational wave)

Status   : ready to use - call compute(m1, m2)
"""
import math

NAME = 'Chirp mass'
SYMBOL = '(m1 m2)^(3/5) / (m1 + m2)^(1/5)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'Mc = (m1 m2)^(3/5) / (m1 + m2)^(1/5)   (the mass combination that sets the leading gravitational wave)'


def compute(m1, m2):
    """the chirp mass in the units of the masses"""
    if m1 <= 0 or m2 <= 0:
        raise ValueError("mass must be positive")
    return (m1 * m2) ** (3 / 5) / (m1 + m2) ** (1 / 5)
