"""Yaw, pitch and roll to quaternion   [yaw pitch roll → q]

Category : Math > Linear algebra
Formula  : q = q_yaw q_pitch q_roll, with q_roll = [cos(r/2), sin(r/2), 0, 0], q_pitch = [cos(p/2), 0, sin(p/2), 0], q_yaw = [cos(y/2), 0, 0, sin(y/2)]

Status   : ready to use - call compute(yaw, pitch, roll)
"""

NAME = 'Yaw, pitch and roll to quaternion'
SYMBOL = 'yaw pitch roll → q'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'q = q_yaw q_pitch q_roll, with q_roll = [cos(r/2), sin(r/2), 0, 0], q_pitch = [cos(p/2), 0, sin(p/2), 0], q_yaw = [cos(y/2), 0, 0, sin(y/2)]'
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


def compute(yaw, pitch, roll):
    """q = q_yaw q_pitch q_roll  (radians; roll about x, pitch about y, yaw about z)"""
    q_yaw = [math.cos(yaw / 2), 0.0, 0.0, math.sin(yaw / 2)]
    q_pitch = [math.cos(pitch / 2), 0.0, math.sin(pitch / 2), 0.0]
    q_roll = [math.cos(roll / 2), math.sin(roll / 2), 0.0, 0.0]
    return _multiply(_multiply(q_yaw, q_pitch), q_roll)
