"""Quaternion to yaw, pitch and roll   [q → yaw pitch roll]

Category : Math > Linear algebra
Formula  : yaw = atan2(2(wz + xy), 1 − 2(y² + z²)),  pitch = asin(2(wy − zx)),  roll = atan2(2(wx + yz), 1 − 2(x² + y²))  (q normalised first)

Status   : ready to use - call compute(q)
"""

NAME = 'Quaternion to yaw, pitch and roll'
SYMBOL = 'q → yaw pitch roll'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'yaw = atan2(2(wz + xy), 1 − 2(y² + z²)),  pitch = asin(2(wy − zx)),  roll = atan2(2(wx + yz), 1 − 2(x² + y²))  (q normalised first)'
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
    """[yaw, pitch, roll] in radians: roll about x, then pitch about y, then yaw about z"""
    q = _quaternion(q)
    s = _size(q)
    if s == 0:
        raise ValueError("the quaternion is zero, it has no yaw, pitch and roll")
    w, x, y, z = [c / s for c in q]
    sine = 2 * (w * y - z * x)
    if abs(sine) > 1 + 1e-9:
        raise ValueError("not a rotation: the pitch sine is outside -1 to 1")
    if abs(sine) >= 1 - 1e-9:
        raise ValueError("gimbal lock: pitch is straight up or straight down, so roll and yaw are not separate")
    return [math.atan2(2 * (w * z + x * y), 1 - 2 * (y * y + z * z)), math.asin(sine),
            math.atan2(2 * (w * x + y * z), 1 - 2 * (x * x + y * y))]
