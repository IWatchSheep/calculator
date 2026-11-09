"""Pigeonhole principle   [⌈n/m⌉]

Category : Math > Discrete and number theory
Formula  : Putting n items in m boxes forces some box to hold at least ⌈n/m⌉ items

Status   : ready to use - call compute(n, m)
"""
import math

NAME = 'Pigeonhole principle'
SYMBOL = '⌈n/m⌉'
CATEGORY = 'Math'
SUBCATEGORY = 'Discrete and number theory'
FORMULA = 'Putting n items in m boxes forces some box to hold at least ⌈n/m⌉ items'


def compute(n, m):
    """Putting n items in m boxes forces some box to hold at least ⌈n/m⌉ items"""
    return math.ceil(n / m)
