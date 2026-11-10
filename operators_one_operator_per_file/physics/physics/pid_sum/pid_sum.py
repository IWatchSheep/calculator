"""PID output   [P + I + D]

Category : Physics > Physics
Formula  : P + I + D   (the sum of the three terms; the menu operator opens four rows joined by →, the answer is the last row)

Status   : ready to use - call compute(p, i, d)
"""
import math

NAME = 'PID output'
SYMBOL = 'P + I + D'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'P + I + D   (the sum of the three terms; the menu operator opens four rows joined by →, the answer is the last row)'


def compute(p, i, d):
    """P + I + D"""
    return p + i + d
