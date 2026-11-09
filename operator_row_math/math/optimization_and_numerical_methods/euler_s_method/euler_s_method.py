"""Row for the operator: Euler's method

Picture:      □ₙ₊₁ = □ₙ + □ · f(□ₙ, □ₙ)
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/optimization_and_numerical_methods/euler_s_method
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = "Euler's method"
KEY = 'math/optimization_and_numerical_methods/euler_s_method'
PATTERN = '□ₙ₊₁ = □ₙ + □ · f(□ₙ, □ₙ)'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['f', 'x0', 'y0', 'h', 'steps']    # what each box (left to right) is
KINDS = ['multi', 'number', 'number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', "Euler's method("), ('box', ''), ('op', ','), ('box', ''), ('op', ','), ('box', ''), ('op', ','), ('box', ''), ('op', ','), ('box', ''), ('op', ')')]      # cards left of "="
RIGHT = [('box', ''), ('op', 'ₙ +'), ('box', ''), ('op', '· f('), ('box', ''), ('op', 'ₙ,'), ('box', ''), ('op', 'ₙ)')]    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)
