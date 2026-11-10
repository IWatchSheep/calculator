"""Dead reckoning   [x + v t along the heading]

Category : Physics > Physics
Formula  : east = x + v cos(heading) t,  north = y + v sin(heading) t   (heading 0 is east, positive turns toward north; a negative speed backs up)

Status   : ready to use - call compute(position, speed, heading, t)
"""
import math

NAME = 'Dead reckoning'
SYMBOL = 'x + v t along the heading'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'east = x + v cos(heading) t,  north = y + v sin(heading) t   (heading 0 is east, positive turns toward north; a negative speed backs up)'


def compute(position, speed, heading, t):
    """the new [east, north] position after t seconds at a speed along a heading"""
    if len(position) != 2:
        raise ValueError("a position has 2 numbers: east, north")
    if t < 0:
        raise ValueError("time cannot be negative")
    return [position[0] + speed * math.cos(heading) * t, position[1] + speed * math.sin(heading) * t]
