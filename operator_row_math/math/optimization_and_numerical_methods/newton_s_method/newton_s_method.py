"""Row for the operator: Newton's method

Picture:      □ = □ − f ( □ ) / f ′ ( □ ) with □ , □
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/optimization_and_numerical_methods/newton_s_method
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = "Newton's method"
KEY = 'math/optimization_and_numerical_methods/newton_s_method'
PATTERN = '□ = □ − f ( □ ) / f ′ ( □ ) with □ , □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['f', 'fprime', 'x0']    # what each box (left to right) is
KINDS = ['function', 'function', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [2, 2, 2, 0, 1]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('box', ''), ('op', '−'), ('op', 'f'), ('op', '('), ('box', ''), ('op', ')'), ('op', '/'), ('op', 'f'), ('op', '′'), ('op', '('), ('box', ''), ('op', ')'), ('op', 'with'), ('box', ''), ('op', ','), ('box', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"))
