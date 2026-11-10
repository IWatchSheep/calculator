"""Schwarzschild radial step   [one proper-time step of r]

Category : Physics > Physics
Formula  : r_next = r + v Δτ + ½ a Δτ²  with  a = −Rs c² / (2 r²)   (one step of a radial fall outside the horizon; returns r only, not the new speed; c = 299792458 m/s)

Status   : ready to use - call compute(r, v, dt, Rs)
"""
import math

NAME = 'Schwarzschild radial step'
SYMBOL = 'one proper-time step of r'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'r_next = r + v Δτ + ½ a Δτ²  with  a = −Rs c² / (2 r²)   (one step of a radial fall outside the horizon; returns r only, not the new speed; c = 299792458 m/s)'


def compute(r, v, dt, Rs):
    """the radius after one proper-time step of a radial fall (v is dr/dτ at the start, negative falls inward)"""
    if r <= 0:
        raise ValueError("a radius must be positive")
    if Rs < 0:
        raise ValueError("the horizon radius cannot be negative")
    if r <= Rs:
        raise ValueError("r is not outside the horizon")
    if dt <= 0:
        raise ValueError("time step must be positive")
    c = 299792458
    a = -(Rs * c * c) / (2 * r * r)
    return r + v * dt + 0.5 * a * dt * dt
