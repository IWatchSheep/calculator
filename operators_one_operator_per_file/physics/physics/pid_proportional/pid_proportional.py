"""PID proportional   [P = Kp e]

Category : Physics > Physics
Formula  : P = Kp e   (the proportional term)

Status   : ready to use - call compute(kp, error)
"""
import math

NAME = 'PID proportional'
SYMBOL = 'P = Kp e'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'P = Kp e   (the proportional term)'


def compute(kp, error):
    """P = Kp e"""
    return kp * error
