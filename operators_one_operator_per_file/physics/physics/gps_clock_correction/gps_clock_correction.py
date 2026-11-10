"""GPS clock correction   [special plus gravitational]

Category : Physics > Physics
Formula  : special + gravitational   (about +38 microseconds per day; the menu operator opens four rows joined by →, the answer is the last row)

Status   : ready to use - call compute(special, gravitational)
"""
import math

NAME = 'GPS clock correction'
SYMBOL = 'special plus gravitational'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'special + gravitational   (about +38 microseconds per day; the menu operator opens four rows joined by →, the answer is the last row)'


def compute(special, gravitational):
    """the correction to add: the kinematic and the gravitational parts together"""
    return special + gravitational
