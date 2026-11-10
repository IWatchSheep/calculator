"""Schwarzschild frequency ratio   [ν_receiver / ν_source]

Category : Physics > Physics
Formula  : ν_receiver / ν_source = √((1 − Rs/r_source) / (1 − Rs/r_receiver))   (between two static clocks outside the horizon; below 1 when the source is deeper, above 1 when the receiver is deeper)

Status   : ready to use - call compute(r_source, r_receiver, Rs)
"""
import math

NAME = 'Schwarzschild frequency ratio'
SYMBOL = 'ν_receiver / ν_source'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'ν_receiver / ν_source = √((1 − Rs/r_source) / (1 − Rs/r_receiver))   (between two static clocks outside the horizon; below 1 when the source is deeper, above 1 when the receiver is deeper)'


def compute(r_source, r_receiver, Rs):
    """the frequency measured at the receiver divided by the frequency sent from the source"""
    if r_source <= 0 or r_receiver <= 0:
        raise ValueError("a radius must be positive")
    if Rs < 0:
        raise ValueError("the horizon radius cannot be negative")
    if r_source <= Rs or r_receiver <= Rs:
        raise ValueError("r is not outside the horizon")
    return math.sqrt((1 - Rs / r_source) / (1 - Rs / r_receiver))
