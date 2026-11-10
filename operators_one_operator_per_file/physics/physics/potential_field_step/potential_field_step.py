"""Potential-field step   [pull plus push]

Category : Physics > Physics
Formula  : F = k_att (goal − position) + F_rep;  inside the influence distance F_rep = k_rep (1/d − 1/influence)(1/d²) u, otherwise 0  (u points from the obstacle toward the robot)

Status   : ready to use - call compute(position, goal, obstacle, influence, k_att, k_rep)
"""
import math

NAME = 'Potential-field step'
SYMBOL = 'pull plus push'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'F = k_att (goal − position) + F_rep;  inside the influence distance F_rep = k_rep (1/d − 1/influence)(1/d²) u, otherwise 0  (u points from the obstacle toward the robot)'


def compute(position, goal, obstacle, influence, k_att, k_rep):
    """one push [Fx, Fy, Fz]: the pull toward the goal plus the push away from a near obstacle"""
    if len(position) != 3 or len(goal) != 3 or len(obstacle) != 3:
        raise ValueError("a point has 3 numbers: x, y, z")
    away = [position[0] - obstacle[0], position[1] - obstacle[1], position[2] - obstacle[2]]
    d = math.sqrt(away[0] * away[0] + away[1] * away[1] + away[2] * away[2])
    if d == 0:
        raise ValueError("the distance is zero")
    if influence <= 0:
        raise ValueError("the influence distance must be positive")
    if k_att < 0 or k_rep < 0:
        raise ValueError("a gain cannot be negative")
    push = k_rep * (1 / d - 1 / influence) * (1 / (d * d)) if d < influence else 0.0
    return [k_att * (goal[k] - position[k]) + push * away[k] / d for k in range(3)]
