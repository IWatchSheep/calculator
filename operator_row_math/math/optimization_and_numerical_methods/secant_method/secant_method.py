"""Row for the operator: Secant method

Picture:      □ₙ₊₁ = □ₙ − f(□ₙ)(□ₙ − □ₙ₋₁) / (f(□ₙ) − f(□ₙ₋₁))
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/optimization_and_numerical_methods/secant_method
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Secant method'
KEY = 'math/optimization_and_numerical_methods/secant_method'
PATTERN = '□ₙ₊₁ = □ₙ − f(□ₙ)(□ₙ − □ₙ₋₁) / (f(□ₙ) − f(□ₙ₋₁))'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['f', 'x0', 'x1']    # what each box (left to right) is
KINDS = ['function', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'secant('), ('box', ''), ('op', ','), ('box', ''), ('op', ','), ('box', ''), ('op', ')')]      # cards left of "="
RIGHT = [('box', ''), ('op', 'ₙ − f('), ('box', ''), ('op', 'ₙ)('), ('box', ''), ('op', 'ₙ −'), ('box', ''), ('op', 'ₙ₋₁) / (f('), ('box', ''), ('op', 'ₙ) − f('), ('box', ''), ('op', 'ₙ₋₁))')]    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)
