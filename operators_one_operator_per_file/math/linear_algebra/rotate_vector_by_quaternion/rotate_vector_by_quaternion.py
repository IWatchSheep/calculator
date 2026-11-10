"""Rotate a vector   [q v q⁻¹]

Category : Math > Linear algebra
Formula  : v turned by q: q v q⁻¹ (the axes stay fixed; a q that is not unit length is allowed)

Status   : ready to use - call compute(q, v)
"""

NAME = 'Rotate a vector'
SYMBOL = 'q v q⁻¹'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'v turned by q: q v q⁻¹ (the axes stay fixed; a q that is not unit length is allowed)'
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


def compute(q, v):
    """turn v by q:  q v q⁻¹  (the scale of q cancels)"""
    q = _quaternion(q)
    if len(v) != 3:
        raise ValueError("a vector has 3 numbers: x, y, z")
    s = q[0] * q[0] + q[1] * q[1] + q[2] * q[2] + q[3] * q[3]
    if s == 0:
        raise ValueError("the quaternion is zero, it cannot rotate a vector")
    r = _multiply(_multiply(q, [0.0, float(v[0]), float(v[1]), float(v[2])]), [q[0], -q[1], -q[2], -q[3]])
    return [r[1] / s, r[2] / s, r[3] / s]
