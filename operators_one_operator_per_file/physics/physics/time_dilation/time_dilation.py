"""Time dilation   [Δt = γΔt₀]

Category : Physics > Physics
Formula  : Δt = Δt₀ / √(1 − v²/c²)   (Δt₀ = time measured by the moving clock)

Status   : ready to use - call compute(dt0, v, c)
"""
import math

NAME = 'Time dilation'
SYMBOL = 'Δt = γΔt₀'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'Δt = Δt₀ / √(1 − v²/c²)   (Δt₀ = time measured by the moving clock)'


def compute(dt0, v, c=299792458):
    """Δt = Δt₀ / √(1 − v²/c²)   (Δt₀ = time measured by the moving clock)"""
    if abs(v) >= c:
        raise ValueError('speed must be less than the speed of light')
    return dt0 / math.sqrt(1 - v ** 2 / c ** 2)
