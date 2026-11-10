"""Rotation matrix from axis and angle   [R(axis, θ)]

Category : Math > Linear algebra
Formula  : the quaternion cos(θ/2) + sin(θ/2) · (the unit axis), then R(q); the axis is normalised first, the angle is in radians

Status   : ready to use - call compute(axis, angle)
"""

NAME = 'Rotation matrix from axis and angle'
SYMBOL = 'R(axis, θ)'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'the quaternion cos(θ/2) + sin(θ/2) · (the unit axis), then R(q); the axis is normalised first, the angle is in radians'
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


def _matrix(q):
    """the rotation matrix of a quaternion that is not zero (normalised here)"""
    s = _size(q)
    w, x, y, z = [c / s for c in q]
    return [[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
            [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
            [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]]


def _three_by_three(R):
    if len(R) != 3 or any(len(row) != 3 for row in R):
        raise ValueError("a rotation matrix has 3 rows of 3 numbers")
    return [[float(c) for c in row] for row in R]


def compute(axis, angle):
    """R(axis, θ): the quaternion of that turn, then its matrix"""
    if len(axis) != 3:
        raise ValueError("a vector has 3 numbers: x, y, z")
    size = math.sqrt(axis[0] * axis[0] + axis[1] * axis[1] + axis[2] * axis[2])
    if size == 0:
        raise ValueError("the axis has length zero")
    s = math.sin(angle / 2)
    return _matrix([math.cos(angle / 2), axis[0] / size * s, axis[1] / size * s, axis[2] / size * s])
