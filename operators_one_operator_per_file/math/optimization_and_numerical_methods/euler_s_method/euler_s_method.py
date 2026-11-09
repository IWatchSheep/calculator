"""Euler's method   [yₙ₊₁ = yₙ + h·f]

Category : Math > Optimization and numerical methods
Formula  : yₙ₊₁ = yₙ + h · f(xₙ, yₙ)   (returns list of (x, y) points)

Status   : ready to use - call compute(f, x0, y0, h, steps)
"""

NAME = "Euler's method"
SYMBOL = 'yₙ₊₁ = yₙ + h·f'
CATEGORY = 'Math'
SUBCATEGORY = 'Optimization and numerical methods'
FORMULA = 'yₙ₊₁ = yₙ + h · f(xₙ, yₙ)   (returns list of (x, y) points)'


def compute(f, x0, y0, h, steps):
    """yₙ₊₁ = yₙ + h · f(xₙ, yₙ)   (returns list of (x, y) points)"""
    points = [(x0, y0)]
    x, y = x0, y0
    for _ in range(steps):
        y += h * f(x, y)
        x += h
        points.append((x, y))
    return points
