"""Bearing between two points   [atan2(north, east)]

Category : Physics > Physics
Formula  : east = sin(Δlon) cos(lat2),  north = cos(lat1) sin(lat2) − sin(lat1) cos(lat2) cos(Δlon),  heading = atan2(north, east)   (0 is east, positive turns toward north)

Status   : ready to use - call compute(lat1, lon1, lat2, lon2)
"""
import math

NAME = 'Bearing between two points'
SYMBOL = 'atan2(north, east)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'east = sin(Δlon) cos(lat2),  north = cos(lat1) sin(lat2) − sin(lat1) cos(lat2) cos(Δlon),  heading = atan2(north, east)   (0 is east, positive turns toward north)'


def compute(lat1, lon1, lat2, lon2):
    """the heading in radians from point 1 to point 2: 0 is east, positive turns toward north"""
    if abs(lat1) > math.pi / 2 or abs(lat2) > math.pi / 2:
        raise ValueError("latitude is past the pole")
    dlon = lon2 - lon1
    east = math.sin(dlon) * math.cos(lat2)
    north = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
    if east == 0 and north == 0:
        raise ValueError("the two points are the same, there is no direction")
    return math.atan2(north, east)
