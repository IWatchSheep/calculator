"""Row for the operator: Convex function

Picture:      f ( □ □ + ( 1 − □ ) □ ) ≤ □ f ( □ ) + ( 1 − □ ) f ( □ ) with □
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/optimization_and_numerical_methods/convex_function
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Convex function'
KEY = 'math/optimization_and_numerical_methods/convex_function'
PATTERN = 'f ( □ □ + ( 1 − □ ) □ ) ≤ □ f ( □ ) + ( 1 − □ ) f ( □ ) with □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['f', 'x', 'y']    # what each box (left to right) is
KINDS = ['function', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [1, 2, 1, 2, 0]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'f'), ('op', '('), ('dec', ''), ('box', ''), ('op', '+'), ('op', '('), ('op', '1'), ('op', '−'), ('dec', ''), ('op', ')'), ('box', ''), ('op', ')'), ('op', '≤'), ('dec', ''), ('op', 'f'), ('op', '('), ('box', ''), ('op', ')'), ('op', '+'), ('op', '('), ('op', '1'), ('op', '−'), ('dec', ''), ('op', ')'), ('op', 'f'), ('op', '('), ('box', ''), ('op', ')'), ('op', 'with'), ('box', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)
