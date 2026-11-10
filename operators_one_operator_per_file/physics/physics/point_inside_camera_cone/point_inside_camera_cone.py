"""Point inside a camera cone   [field of view]

Category : Physics > Physics
Formula  : 1 when v · d > 0 and (v · d) / (|v| |d|) ≥ cos α, with v = p − c (the camera c looks along d with half-angle α; the edge counts as inside); 0 otherwise

Status   : ready to use - call compute(camera, direction, half_angle, point)
"""
import math

NAME = 'Point inside a camera cone'
SYMBOL = 'field of view'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = '1 when v · d > 0 and (v · d) / (|v| |d|) ≥ cos α, with v = p − c (the camera c looks along d with half-angle α; the edge counts as inside); 0 otherwise'


def compute(camera, direction, half_angle, point):
    """1 if the point is inside the camera's cone of view, 0 if outside"""
    if len(camera) != 3 or len(direction) != 3 or len(point) != 3:
        raise ValueError("a point has 3 numbers: x, y, z")
    d_size = math.sqrt(direction[0] * direction[0] + direction[1] * direction[1] + direction[2] * direction[2])
    if d_size == 0:
        raise ValueError("the look direction has length zero")
    v = [point[0] - camera[0], point[1] - camera[1], point[2] - camera[2]]
    v_size = math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])
    if v_size == 0:
        raise ValueError("the point is the camera")
    if not 0 <= half_angle <= math.pi:
        raise ValueError("the field of view must be from 0 to pi")
    along = v[0] * direction[0] + v[1] * direction[1] + v[2] * direction[2]
    return 1 if along > 0 and along / (v_size * d_size) >= math.cos(half_angle) - 1e-12 else 0
