"""Relativistic Doppler: beta   [β = v/c]

Category : Physics > Physics
Formula  : β = v / c   (v > 0 receding, v < 0 approaching; the speed must be less than the speed of light)

Status   : ready to use - call compute(v, c=299792458)
"""

NAME = 'Relativistic Doppler: beta'
SYMBOL = 'β = v/c'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'β = v / c   (v > 0 receding, v < 0 approaching; the speed must be less than the speed of light)'


def compute(v, c=299792458):
    """β = v / c"""
    if abs(v) >= c:
        raise ValueError('speed must be less than the speed of light')
    return v / c
