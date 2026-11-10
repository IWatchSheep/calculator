"""Local east, north, up   [a small GPS step on the flat Earth]

Category : Physics > Physics
Formula  : east = 6371000 cos(lat) Δlon,  north = 6371000 Δlat,  up = Δheight   (radians and metres; the flat patch, not the haversine arc)

Status   : ready to use - call compute(lat, delta_lat, delta_lon, delta_height)
"""
import math

NAME = 'Local east, north, up'
SYMBOL = 'a small GPS step on the flat Earth'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'east = 6371000 cos(lat) Δlon,  north = 6371000 Δlat,  up = Δheight   (radians and metres; the flat patch, not the haversine arc)'


def compute(lat, delta_lat, delta_lon, delta_height):
    """[east, north, up] in metres for a small change of latitude, longitude and height"""
    if abs(lat) > math.pi / 2:
        raise ValueError("latitude is past the pole")
    return [6371000 * math.cos(lat) * delta_lon, 6371000 * delta_lat, delta_height]
