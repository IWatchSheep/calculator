"""Row for the operator: Half angle

Picture:      sin ( □ / 2 ) = √ ( ( 1 − cos ( □ ) ) / 2 )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py math/trigonometry/half_angle
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Half angle'
KEY = 'math/trigonometry/half_angle'
PATTERN = 'sin ( □ / 2 ) = √ ( ( 1 − cos ( □ ) ) / 2 )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['theta']    # what each box (left to right) is
KINDS = ['number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 0]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'sin'), ('op', '('), ('box', ''), ('op', '/'), ('op', '2'), ('op', ')'), ('op', '='), ('op', '√'), ('op', '('), ('op', '('), ('op', '1'), ('op', '−'), ('op', 'cos'), ('op', '('), ('box', ''), ('op', ')'), ('op', ')'), ('op', '/'), ('op', '2'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"))
