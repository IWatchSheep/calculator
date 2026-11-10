"""Haversine distance   [great-circle distance]

Category : Physics > Physics
Formula  : a = sin²(Δlat/2) + cos(lat1) cos(lat2) sin²(Δlon/2),  d = 6371000 · 2 atan2(√a, √(1 − a))   (Earth radius 6371000 m, angles in radians)

Status   : ready to use - call compute(lat1, lon1, lat2, lon2)
"""
import math

NAME = 'Haversine distance'
SYMBOL = 'great-circle distance'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'a = sin²(Δlat/2) + cos(lat1) cos(lat2) sin²(Δlon/2),  d = 6371000 · 2 atan2(√a, √(1 − a))   (Earth radius 6371000 m, angles in radians)'


def compute(lat1, lon1, lat2, lon2):
    """the distance in metres along the Earth's surface between two latitude / longitude points"""
    if abs(lat1) > math.pi / 2 or abs(lat2) > math.pi / 2:
        raise ValueError("latitude is past the pole")
    s1 = math.sin((lat2 - lat1) / 2)
    s2 = math.sin((lon2 - lon1) / 2)
    a = s1 * s1 + math.cos(lat1) * math.cos(lat2) * s2 * s2
    a = min(max(a, 0.0), 1.0)
    return 6371000 * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
