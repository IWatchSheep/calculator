"""Epsilon-delta continuity   [ε–δ]

Category : Math > Real analysis
Formula  : f is continuous at a if ∀ε>0 ∃δ>0: |x − a| < δ ⇒ |f(x) − f(a)| < ε

Status   : ready to use - call compute(f, a, eps)
"""

NAME = 'Epsilon-delta continuity'
SYMBOL = 'ε–δ'
CATEGORY = 'Math'
SUBCATEGORY = 'Real analysis'
FORMULA = 'f is continuous at a if ∀ε>0 ∃δ>0: |x − a| < δ ⇒ |f(x) − f(a)| < ε'
import math
from operators_one_operator_per_file import _helpers as H


def compute(f, a, eps):
    """A δ that works at a for the given ε: |x − a| < δ ⇒ |f(x) − f(a)| < ε  (searched numerically)"""
    delta = 1.0
    for _ in range(60):
        if all(abs(f(a + delta * k / 200) - f(a)) < eps for k in range(-199, 200)):
            return delta
        delta /= 2
    raise ValueError("no δ found: f may not be continuous at a")
