"""Kerr inner horizon   [r− = Rs/2 − √((Rs/2)² − a²)]

Category : Physics > Physics
Formula  : r− = Rs/2 − √((Rs/2)² − a²)   (the smaller horizon of a spinning mass; a = J/(M c) in metres; a = 0 gives r− = 0; |a| ≤ Rs/2)

Status   : ready to use - call compute(Rs, a)
"""
import math

NAME = 'Kerr inner horizon'
SYMBOL = 'r− = Rs/2 − √((Rs/2)² − a²)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'r− = Rs/2 − √((Rs/2)² − a²)   (the smaller horizon of a spinning mass; a = J/(M c) in metres; a = 0 gives r− = 0; |a| ≤ Rs/2)'


def compute(Rs, a):
    """r− = Rs/2 − √((Rs/2)² − a²)"""
    if Rs <= 0:
        raise ValueError("the horizon radius must be positive")
    if abs(a) > Rs / 2:
        raise ValueError("the spin is past the extreme Kerr limit")
    h = Rs / 2
    return h - math.sqrt(h * h - a * a)
