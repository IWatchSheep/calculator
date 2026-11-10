"""Quaternion inverse   [q⁻¹]

Category : Math > Linear algebra
Formula  : q⁻¹ = q* / (w² + x² + y² + z²)

Status   : ready to use - call compute(q)
"""

NAME = 'Quaternion inverse'
SYMBOL = 'q⁻¹'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'q⁻¹ = q* / (w² + x² + y² + z²)'
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


def compute(q):
    """q⁻¹ = conjugate divided by the square of the size"""
    w, x, y, z = _quaternion(q)
    s = w * w + x * x + y * y + z * z
    if s == 0:
        raise ValueError("the quaternion is zero, it has no inverse")
    return [w / s, -x / s, -y / s, -z / s]
