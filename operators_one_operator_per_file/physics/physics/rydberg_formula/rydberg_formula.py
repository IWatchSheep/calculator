"""Rydberg formula   [1/λ = RZ²(1/n₁² − 1/n₂²)]

Category : Physics > Physics
Formula  : λ = 1 / ( R Z² (1/n₁² − 1/n₂²) )   (n₂ > n₁, R = 1.0973731568×10⁷ /m)

Status   : ready to use - call compute(n1, n2, Z, R)
"""
import math

NAME = 'Rydberg formula'
SYMBOL = '1/λ = RZ²(1/n₁² − 1/n₂²)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'λ = 1 / ( R Z² (1/n₁² − 1/n₂²) )   (n₂ > n₁, R = 1.0973731568×10⁷ /m)'


def compute(n1, n2, Z=1, R=10973731.568160):
    """λ = 1 / ( R Z² (1/n₁² − 1/n₂²) )   (n₂ > n₁, R = 1.0973731568×10⁷ /m)"""
    if n2 <= n1:
        raise ValueError('n2 must be larger than n1')
    return 1 / (R * Z ** 2 * (1 / n1 ** 2 - 1 / n2 ** 2))
