"""Convolution   [f ∗ g]

Category : Math > Transforms and differential equations
Formula  : (f ∗ g)[k] = Σⱼ f[j] · g[k − j]

Status   : ready to use - call compute(f, g)
"""

NAME = 'Convolution'
SYMBOL = 'f ∗ g'
CATEGORY = 'Math'
SUBCATEGORY = 'Transforms and differential equations'
FORMULA = '(f ∗ g)[k] = Σⱼ f[j] · g[k − j]'


def compute(f, g):
    """(f ∗ g)[k] = Σⱼ f[j] · g[k − j]"""
    return [sum(f[j] * g[k - j] for j in range(len(f)) if 0 <= k - j < len(g)) for k in range(len(f) + len(g) - 1)]
