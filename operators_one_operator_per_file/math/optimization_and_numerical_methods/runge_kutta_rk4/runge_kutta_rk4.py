"""Runge-Kutta (RK4)   [RK4]

Category : Math > Optimization and numerical methods
Formula  : yₙ₊₁ = yₙ + h/6 · (k₁ + 2k₂ + 2k₃ + k₄)

Status   : ready to use - call compute(f, x0, y0, h, steps)
"""

NAME = 'Runge-Kutta (RK4)'
SYMBOL = 'RK4'
CATEGORY = 'Math'
SUBCATEGORY = 'Optimization and numerical methods'
FORMULA = 'yₙ₊₁ = yₙ + h/6 · (k₁ + 2k₂ + 2k₃ + k₄)'


def compute(f, x0, y0, h, steps):
    """yₙ₊₁ = yₙ + h/6 · (k₁ + 2k₂ + 2k₃ + k₄)"""
    points = [(x0, y0)]
    x, y = x0, y0
    for _ in range(steps):
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h * k1 / 2)
        k3 = f(x + h / 2, y + h * k2 / 2)
        k4 = f(x + h, y + h * k3)
        y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
        points.append((x, y))
    return points
