"""Time to collision   [distance / closing speed]

Category : Physics > Physics
Formula  : t = |r| / (−(r · v) / |r|)   (r is the obstacle minus the robot, v the robot's velocity; only when the closing speed is positive)

Status   : ready to use - call compute(position, velocity)
"""
import math

NAME = 'Time to collision'
SYMBOL = 'distance / closing speed'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = "t = |r| / (−(r · v) / |r|)   (r is the obstacle minus the robot, v the robot's velocity; only when the closing speed is positive)"


def compute(position, velocity):
    """seconds until the robot reaches a fixed obstacle, when it is approaching"""
    if len(position) != 3 or len(velocity) != 3:
        raise ValueError("a vector has 3 numbers: x, y, z")
    distance = math.sqrt(position[0] * position[0] + position[1] * position[1] + position[2] * position[2])
    if distance == 0:
        raise ValueError("the distance is zero")
    closing = -(position[0] * velocity[0] + position[1] * velocity[1] + position[2] * velocity[2]) / distance
    if closing <= 0:
        raise ValueError("not approaching")
    return distance / closing
