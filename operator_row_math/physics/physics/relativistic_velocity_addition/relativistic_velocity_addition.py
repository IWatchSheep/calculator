"""Row for the operator: Relativistic velocity addition

Picture:      □ = ( □ + □ ) / ( 1 + □ × □ / c ² )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/relativistic_velocity_addition
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Relativistic velocity addition'
KEY = 'physics/physics/relativistic_velocity_addition'
PATTERN = '□ = ( □ + □ ) / ( 1 + □ × □ / c ² )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['u', 'v']    # what each box (left to right) is
KINDS = ['number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 1, 0, 1]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '('), ('box', ''), ('op', '+'), ('box', ''), ('op', ')'), ('op', '/'), ('op', '('), ('op', '1'), ('op', '+'), ('box', ''), ('op', '×'), ('box', ''), ('op', '/'), ('op', 'c'), ('op', '²'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)
