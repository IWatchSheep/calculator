"""Quaternion multiply   [q₁ q₂]

Category : Math > Linear algebra
Formula  : Hamilton product of two quaternions (w, x, y, z), the second turn done first

Status   : ready to use - call compute(q1, q2)
"""

NAME = 'Quaternion multiply'
SYMBOL = 'q₁ q₂'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'Hamilton product of two quaternions (w, x, y, z), the second turn done first'
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


def compute(q1, q2):
    """Hamilton product q₁ q₂ of two quaternions [w, x, y, z]"""
    return _multiply(_quaternion(q1), _quaternion(q2))
