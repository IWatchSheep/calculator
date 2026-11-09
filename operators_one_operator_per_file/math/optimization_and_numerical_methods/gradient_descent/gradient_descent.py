"""Gradient descent   [xₖ₊₁ = xₖ − η∇f]

Category : Math > Optimization and numerical methods
Formula  : Repeat xₖ₊₁ = xₖ − η ∇f(xₖ)

Status   : ready to use - call compute(grad_f, x0, lr=0.01, steps=1000)
"""

NAME = 'Gradient descent'
SYMBOL = 'xₖ₊₁ = xₖ − η∇f'
CATEGORY = 'Math'
SUBCATEGORY = 'Optimization and numerical methods'
FORMULA = 'Repeat xₖ₊₁ = xₖ − η ∇f(xₖ)'


def compute(grad_f, x0, lr=0.01, steps=1000):
    """Repeat xₖ₊₁ = xₖ − η ∇f(xₖ)"""
    x = list(x0)
    for _ in range(steps):
        g = grad_f(x)
        x = [xi - lr * gi for xi, gi in zip(x, g)]
    return x
