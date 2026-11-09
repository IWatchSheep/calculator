"""Bisection method   [bisect]

Category : Math > Optimization and numerical methods
Formula  : Repeatedly halve [a, b] keeping the half where f changes sign

Status   : ready to use - call compute(f, a, b, tol=1e-12, max_iter=200)
"""

NAME = 'Bisection method'
SYMBOL = 'bisect'
CATEGORY = 'Math'
SUBCATEGORY = 'Optimization and numerical methods'
FORMULA = 'Repeatedly halve [a, b] keeping the half where f changes sign'


def compute(f, a, b, tol=1e-12, max_iter=200):
    """Repeatedly halve [a, b] keeping the half where f changes sign"""
    fa = f(a)
    if fa * f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    for _ in range(max_iter):
        mid = (a + b) / 2
        fm = f(mid)
        if abs(fm) < tol or (b - a) / 2 < tol:
            return mid
        if fa * fm < 0:
            b = mid
        else:
            a, fa = mid, fm
    return (a + b) / 2
