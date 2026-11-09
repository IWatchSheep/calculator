"""Gradient   [∇]

Category : Math > Calculus
Formula  : ∇f = (∂f/∂x₁, …, ∂f/∂xₙ)   (numerical)

Status   : ready to use - call compute(f, point, h=1e-6)
"""

NAME = 'Gradient'
SYMBOL = '∇'
CATEGORY = 'Math'
SUBCATEGORY = 'Calculus'
FORMULA = '∇f = (∂f/∂x₁, …, ∂f/∂xₙ)   (numerical)'


def compute(f, point, h=1e-6):
    """∇f = (∂f/∂x₁, …, ∂f/∂xₙ)   (numerical)"""
    return [(f(*[p + h if j == i else p for j, p in enumerate(point)]) - f(*[p - h if j == i else p for j, p in enumerate(point)])) / (2 * h) for i in range(len(point))]
