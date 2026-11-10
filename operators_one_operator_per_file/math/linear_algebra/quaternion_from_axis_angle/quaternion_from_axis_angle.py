"""Quaternion from axis and angle   [axis θ]

Category : Math > Linear algebra
Formula  : q = cos(θ/2) + sin(θ/2) · (the unit axis)

Status   : ready to use - call compute(axis, angle)
"""

NAME = 'Quaternion from axis and angle'
SYMBOL = 'axis θ'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'q = cos(θ/2) + sin(θ/2) · (the unit axis)'
import math


def _quaternion(q):
    if len(q) != 4:
        raise ValueError("a quaternion has 4 numbers: w, x, y, z")
    return [float(c) for c in q]


def _multiply(p, q):
    return [p[0] * q[0] - p[1] * q[1] - p[2] * q[2] - p[3] * q[3],
            p[0] * q[1] + p[1] * q[0] + p[2] * q[3] - p[3] * q[2],
            p[0] * q[2] - p[1] * q[3] + p[2] * q[0] + p[3] * q[1],
            p[0] * q[3] + p[1] * q[2] - p[2] * q[1] + p[3] * q[0]]


def _size(q):
    return math.sqrt(q[0] * q[0] + q[1] * q[1] + q[2] * q[2] + q[3] * q[3])


def compute(axis, angle):
    """q = [cos(θ/2), sin(θ/2) · û]; the axis is normalised first, the angle is in radians"""
    if len(axis) != 3:
        raise ValueError("a vector has 3 numbers: x, y, z")
    size = math.sqrt(axis[0] * axis[0] + axis[1] * axis[1] + axis[2] * axis[2])
    if size == 0:
        raise ValueError("the axis has length zero")
    s = math.sin(angle / 2)
    return [math.cos(angle / 2), axis[0] / size * s, axis[1] / size * s, axis[2] / size * s]
