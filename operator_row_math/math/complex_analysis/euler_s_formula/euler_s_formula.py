"""Row for the operator: Euler's formula

Picture:      e ^ ( i □ ) = cos □ + i sin □
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py math/complex_analysis/euler_s_formula
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = "Euler's formula"
KEY = 'math/complex_analysis/euler_s_formula'
PATTERN = 'e ^ ( i □ ) = cos □ + i sin □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['theta']    # what each box (left to right) is
KINDS = ['number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 0, 0]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'e'), ('op', '^'), ('op', '('), ('op', 'i'), ('box', ''), ('op', ')'), ('op', '='), ('op', 'cos'), ('box', ''), ('op', '+'), ('op', 'i'), ('op', 'sin'), ('box', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"))
