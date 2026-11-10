"""Row for the operator: Midpoint formula

Picture:      □ = ( ( □ ₁ + □ ₂ ) / 2 , ( □ ₁ + □ ₂ ) / 2 )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py geometry/geometry/midpoint_formula
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Midpoint formula'
KEY = 'geometry/geometry/midpoint_formula'
PATTERN = '□ = ( ( □ ₁ + □ ₂ ) / 2 , ( □ ₁ + □ ₂ ) / 2 )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['x1', 'y1', 'x2', 'y2']    # what each box (left to right) is
KINDS = ['number', 'number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 2, 1, 3]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
LEVELS = [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
FRAC = [[], [], [], [[1, 'hide']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'hide']], [[1, 'bar']], [[1, 'd']], [], [[2, 'hide']], [[2, 'n']], [[2, 'n']], [[2, 'n']], [[2, 'n']], [[2, 'n']], [[2, 'hide']], [[2, 'bar']], [[2, 'd']], []]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '('), ('op', '('), ('box', ''), ('op', '1'), ('op', '+'), ('box', ''), ('op', '2'), ('op', ')'), ('op', '/'), ('op', '2'), ('op', ','), ('op', '('), ('box', ''), ('op', '1'), ('op', '+'), ('box', ''), ('op', '2'), ('op', ')'), ('op', '/'), ('op', '2'), ('op', ')')]      # cards left of "="
RIGHT = []


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
