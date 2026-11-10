"""Quaternion from a rotation matrix   [q(R)]

Category : Math > Linear algebra
Formula  : Shepperd's method: the largest of w, x, y, z is found first; the answer has w ≥ 0

Status   : ready to use - call compute(R)
"""

NAME = 'Quaternion from a rotation matrix'
SYMBOL = 'q(R)'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = "Shepperd's method: the largest of w, x, y, z is found first; the answer has w ≥ 0"
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


def compute(R):
    """[w, x, y, z] of a rotation matrix (w ≥ 0); anything that is not a rotation is declined"""
    R = _three_by_three(R)
    for i in range(3):
        for j in range(3):
            dot = R[i][0] * R[j][0] + R[i][1] * R[j][1] + R[i][2] * R[j][2]
            if abs(dot - (1.0 if i == j else 0.0)) > 1e-8:
                raise ValueError("not a rotation matrix")
    det = (R[0][0] * (R[1][1] * R[2][2] - R[1][2] * R[2][1]) - R[0][1] * (R[1][0] * R[2][2] - R[1][2] * R[2][0])
           + R[0][2] * (R[1][0] * R[2][1] - R[1][1] * R[2][0]))
    if abs(det - 1) > 1e-8:
        raise ValueError("not a rotation matrix")
    trace = R[0][0] + R[1][1] + R[2][2]
    if trace > 0:
        s = math.sqrt(trace + 1) * 2
        q = [0.25 * s, (R[2][1] - R[1][2]) / s, (R[0][2] - R[2][0]) / s, (R[1][0] - R[0][1]) / s]
    elif R[0][0] > R[1][1] and R[0][0] > R[2][2]:
        s = math.sqrt(1 + R[0][0] - R[1][1] - R[2][2]) * 2
        q = [(R[2][1] - R[1][2]) / s, 0.25 * s, (R[0][1] + R[1][0]) / s, (R[0][2] + R[2][0]) / s]
    elif R[1][1] > R[2][2]:
        s = math.sqrt(1 + R[1][1] - R[0][0] - R[2][2]) * 2
        q = [(R[0][2] - R[2][0]) / s, (R[0][1] + R[1][0]) / s, 0.25 * s, (R[1][2] + R[2][1]) / s]
    else:
        s = math.sqrt(1 + R[2][2] - R[0][0] - R[1][1]) * 2
        q = [(R[1][0] - R[0][1]) / s, (R[0][2] + R[2][0]) / s, (R[1][2] + R[2][1]) / s, 0.25 * s]
    if q[0] < 0:
        q = [-c for c in q]
    return [c + 0.0 for c in q]
