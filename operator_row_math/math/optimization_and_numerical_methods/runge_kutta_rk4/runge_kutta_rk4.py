"""Row for the operator: Runge-Kutta (RK4)

Picture:      □ ₙ₊₁ = □ ₙ + □ / 6 · ( □ ₁ + 2 □ ₂ + 2 □ ₃ + □ ₄ ) with □ , □ , □
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/optimization_and_numerical_methods/runge_kutta_rk4
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Runge-Kutta (RK4)'
KEY = 'math/optimization_and_numerical_methods/runge_kutta_rk4'
PATTERN = '□ ₙ₊₁ = □ ₙ + □ / 6 · ( □ ₁ + 2 □ ₂ + 2 □ ₃ + □ ₄ ) with □ , □ , □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['f', 'x0', 'y0', 'h', 'steps']    # what each box (left to right) is
KINDS = ['multi', 'number', 'number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [2, 3, 0, 1, 4]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', 'ₙ₊₁'), ('op', '='), ('box', ''), ('op', 'ₙ'), ('op', '+'), ('box', ''), ('op', '/'), ('op', '6'), ('op', '·'), ('op', '('), ('dec', ''), ('op', '₁'), ('op', '+'), ('op', '2'), ('dec', ''), ('op', '₂'), ('op', '+'), ('op', '2'), ('dec', ''), ('op', '₃'), ('op', '+'), ('dec', ''), ('op', '₄'), ('op', ')'), ('op', 'with'), ('box', ''), ('op', ','), ('box', ''), ('op', ','), ('box', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)
