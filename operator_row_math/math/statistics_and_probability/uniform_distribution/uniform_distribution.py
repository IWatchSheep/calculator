"""Row for the operator: Uniform distribution

Picture:      f ( □ ) = 1 / ( □ − □ ) for □ ≤ □ ≤ □ , else 0
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py math/statistics_and_probability/uniform_distribution
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Uniform distribution'
KEY = 'math/statistics_and_probability/uniform_distribution'
PATTERN = 'f ( □ ) = 1 / ( □ − □ ) for □ ≤ □ ≤ □ , else 0'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['x', 'a', 'b']    # what each box (left to right) is
KINDS = ['number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 2, 1, 1, 0, 2]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'f'), ('op', '('), ('box', ''), ('op', ')'), ('op', '='), ('op', '1'), ('op', '/'), ('op', '('), ('box', ''), ('op', '−'), ('box', ''), ('op', ')'), ('op', 'for'), ('box', ''), ('op', '≤'), ('box', ''), ('op', '≤'), ('box', ''), ('op', ','), ('op', 'else'), ('op', '0')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"))
