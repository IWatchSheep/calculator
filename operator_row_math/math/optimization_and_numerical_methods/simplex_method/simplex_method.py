"""Row for the operator: Simplex method

Picture:      simplex ( □ · □ ≤ □ ) with □ = □
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/optimization_and_numerical_methods/simplex_method
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Simplex method'
KEY = 'math/optimization_and_numerical_methods/simplex_method'
PATTERN = 'simplex ( □ · □ ≤ □ ) with □ = □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['c', 'A', 'b']    # what each box (left to right) is
KINDS = ['list', 'matrix', 'list']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [1, 2, 0]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'simplex'), ('op', '('), ('box', ''), ('op', '·'), ('dec', ''), ('op', '≤'), ('box', ''), ('op', ')'), ('op', 'with'), ('box', '')]      # cards left of "="
RIGHT = [('box', '')]    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"))
