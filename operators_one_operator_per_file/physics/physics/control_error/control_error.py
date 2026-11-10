"""Control error   [e = setpoint − measured]

Category : Physics > Physics
Formula  : e = setpoint − measured   (positive means too low)

Status   : ready to use - call compute(setpoint, measured)
"""
import math

NAME = 'Control error'
SYMBOL = 'e = setpoint − measured'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'e = setpoint − measured   (positive means too low)'


def compute(setpoint, measured):
    """e = setpoint − measured"""
    return setpoint - measured
