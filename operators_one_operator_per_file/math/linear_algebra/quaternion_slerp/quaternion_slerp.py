"""Quaternion blend   [slerp]

Category : Math > Linear algebra
Formula  : slerp(q₀, q₁, t) = (sin((1 − t)ω) q₀ + sin(tω) q₁) / sin ω, ω = acos(q₀ · q₁); the short way round (q and −q are the same turn)

Status   : ready to use - call compute(q0, q1, t)
"""

NAME = 'Quaternion blend'
SYMBOL = 'slerp'
CATEGORY = 'Math'
SUBCATEGORY = 'Linear algebra'
FORMULA = 'slerp(q₀, q₁, t) = (sin((1 − t)ω) q₀ + sin(tω) q₁) / sin ω, ω = acos(q₀ · q₁); the short way round (q and −q are the same turn)'
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


def compute(q0, q1, t):
    """the orientation a fraction t of the short turn from q0 to q1"""
    q0, q1 = _quaternion(q0), _quaternion(q1)
    s0, s1 = _size(q0), _size(q1)
    if s0 == 0 or s1 == 0:
        raise ValueError("the quaternion is zero, it cannot be blended")
    if not 0 <= t <= 1:
        raise ValueError("the blend is outside 0 to 1")
    a = [c / s0 for c in q0]
    b = [c / s1 for c in q1]
    d = a[0] * b[0] + a[1] * b[1] + a[2] * b[2] + a[3] * b[3]
    if d < 0:
        b = [-c for c in b]
        d = -d
    d = min(d, 1.0)
    if d > 0.9995:
        r = [a[k] + t * (b[k] - a[k]) for k in range(4)]
        s = _size(r)
        return [c / s for c in r]
    omega = math.acos(d)
    k0 = math.sin((1 - t) * omega) / math.sin(omega)
    k1 = math.sin(t * omega) / math.sin(omega)
    return [k0 * a[k] + k1 * b[k] for k in range(4)]
