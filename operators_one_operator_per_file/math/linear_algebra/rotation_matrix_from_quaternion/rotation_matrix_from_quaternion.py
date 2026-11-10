"""Rotation matrix from a quaternion   [R(q)]

Category : Math > Linear algebra
Formula  : R(q) from the normalised quaternion (w, x, y, z): [1 − 2(y² + z²), 2(xy − zw), 2(xz + yw)], [2(xy + zw), 1 − 2(x² + z²), 2(yz − xw)], [2(xz − yw), 2(yz + xw), 1 − 2(x² + y²)]

Status   : ready to use - call compute(q)
"""

NAME = 'Rotation matrix from a quaternion'
SYMBOL = 'R(q)'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'R(q) from the normalised quaternion (w, x, y, z): [1 − 2(y² + z²), 2(xy − zw), 2(xz + yw)], [2(xy + zw), 1 − 2(x² + z²), 2(yz − xw)], [2(xz − yw), 2(yz + xw), 1 − 2(x² + y²)]'
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


def compute(q):
    """the 3 × 3 rotation matrix of the quaternion q (normalised first)"""
    q = _quaternion(q)
    if _size(q) == 0:
        raise ValueError("the quaternion is zero, it cannot be a rotation")
    return _matrix(q)
