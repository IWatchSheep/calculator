"""Rotation matrix from yaw, pitch and roll   [R(yaw, pitch, roll)]

Category : Math > Linear algebra
Formula  : the quaternion q_yaw q_pitch q_roll, then R(q)

Status   : ready to use - call compute(yaw, pitch, roll)
"""

NAME = 'Rotation matrix from yaw, pitch and roll'
SYMBOL = 'R(yaw, pitch, roll)'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'the quaternion q_yaw q_pitch q_roll, then R(q)'
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


def compute(yaw, pitch, roll):
    """R(yaw, pitch, roll): radians; roll about x, pitch about y, yaw about z"""
    q_yaw = [math.cos(yaw / 2), 0.0, 0.0, math.sin(yaw / 2)]
    q_pitch = [math.cos(pitch / 2), 0.0, math.sin(pitch / 2), 0.0]
    q_roll = [math.cos(roll / 2), math.sin(roll / 2), 0.0, 0.0]
    return _matrix(_multiply(_multiply(q_yaw, q_pitch), q_roll))
