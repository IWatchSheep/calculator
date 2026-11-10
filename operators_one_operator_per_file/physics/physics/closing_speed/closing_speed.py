"""Closing speed   [−(r · v) / |r|]

Category : Physics > Physics
Formula  : −(r · v) / |r|   (how fast the distance to a fixed obstacle is shrinking; positive means approaching)

Status   : ready to use - call compute(position, velocity)
"""
import math

NAME = 'Closing speed'
SYMBOL = '−(r · v) / |r|'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = '−(r · v) / |r|   (how fast the distance to a fixed obstacle is shrinking; positive means approaching)'


def compute(position, velocity):
    """metres per second the distance to a fixed obstacle is shrinking"""
    if len(position) != 3 or len(velocity) != 3:
        raise ValueError("a vector has 3 numbers: x, y, z")
    distance = math.sqrt(position[0] * position[0] + position[1] * position[1] + position[2] * position[2])
    if distance == 0:
        raise ValueError("the distance is zero")
    closing = -(position[0] * velocity[0] + position[1] * velocity[1] + position[2] * velocity[2]) / distance
    return closing
