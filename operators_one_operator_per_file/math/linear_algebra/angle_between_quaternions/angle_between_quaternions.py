"""Angle between two orientations   [∠(q₀, q₁)]

Category : Math > Linear algebra
Formula  : ∠ = 2 acos(|q₀ · q₁|) with both quaternions normalised (q and −q are the same orientation), from 0 to π radians

Status   : ready to use - call compute(q0, q1)
"""

NAME = 'Angle between two orientations'
SYMBOL = '∠(q₀, q₁)'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = '∠ = 2 acos(|q₀ · q₁|) with both quaternions normalised (q and −q are the same orientation), from 0 to π radians'
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


def compute(q0, q1):
    """the smallest turn, in radians, that takes orientation q0 to q1"""
    q0, q1 = _quaternion(q0), _quaternion(q1)
    s0, s1 = _size(q0), _size(q1)
    if s0 == 0 or s1 == 0:
        raise ValueError("the quaternion is zero, it has no orientation")
    a = [c / s0 for c in q0]
    b = [c / s1 for c in q1]
    d = min(abs(a[0] * b[0] + a[1] * b[1] + a[2] * b[2] + a[3] * b[3]), 1.0)
    return 2 * math.acos(d)
