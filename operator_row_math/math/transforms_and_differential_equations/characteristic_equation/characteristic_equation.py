"""Row for the operator: Characteristic equation

Picture:      □ r ² + □ r + □ = 0
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py math/transforms_and_differential_equations/characteristic_equation
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Characteristic equation'
KEY = 'math/transforms_and_differential_equations/characteristic_equation'
PATTERN = '□ r ² + □ r + □ = 0'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['a', 'b', 'c']    # what each box (left to right) is
KINDS = ['number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
LEVELS = [0, 0, -1, 0, 0, 0, 0, 0, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('box', ''), ('op', 'r'), ('op', '2'), ('op', '+'), ('box', ''), ('op', 'r'), ('op', '+'), ('box', ''), ('op', '='), ('op', '0')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"))
